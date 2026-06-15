#!/usr/bin/env python3
"""Validate pack structure AND definition content for illo-characters.

Stdlib only; run from anywhere. CI runs this on every PR and push to main.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PACKS = ROOT / "packs"
REQUIRED = ("character.md", "reference.png", "preview.png")
HEADINGS = ("## Locked design", "## Prompt spec", "## Value rules")
LOOKS = {"riso", "blueprint", "woodcut", "pixel",
         "clay", "manila", "chalk", "phosphor", "enamel", "gouache",
         "felt"}
RESERVED = {"blot", "illo"} | LOOKS
KEBAB = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
SEMVER = re.compile(r"\d+\.\d+\.\d+")
STYLE_RE = re.compile(r"^Style:\s*\**([a-z0-9-]+)\**\s*$", re.M)
ALIASES_RE = re.compile(r"^Aliases:\s*(.+)$", re.M)
MAX_MD = 16 * 1024
MAX_PNG = 3 * 1024 * 1024
MAX_DESC = 200
MIN_PX = 512
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

errors = []


def png_size(b):
    """(width, height) from PNG bytes, or (None, None)."""
    if b[:8] == PNG_MAGIC and b[12:16] == b"IHDR":
        return int.from_bytes(b[16:20], "big"), int.from_bytes(b[20:24], "big")
    return None, None


def section(text, heading):
    """The body of a markdown section, up to the next ## heading."""
    m = re.search(rf"^{re.escape(heading)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


packs = sorted(d for d in PACKS.iterdir() if d.is_dir()) if PACKS.is_dir() else []
if not packs:
    errors.append("packs/ is missing or empty")

readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").is_file() else ""
declared_styles = {}
declared_aliases = {}

for d in packs:
    name = d.name
    if not KEBAB.fullmatch(name):
        errors.append(f"{name}: pack name is not lowercase kebab-case")
    if name in RESERVED:
        errors.append(f"{name}: pack name is reserved (shipped character or look name)")
    for f in REQUIRED:
        if not (d / f).is_file():
            errors.append(f"{name}: missing {f}")
    for f in d.iterdir():
        if f.name.startswith(".") or f.suffix not in (".md", ".png"):
            errors.append(f"{name}: disallowed file {f.name} (only .md/.png)")
    if f"](packs/{name}/)" not in readme:
        errors.append(f"{name}: no row in the README catalog table")

    md = d / "character.md"
    if md.is_file():
        if md.stat().st_size > MAX_MD:
            errors.append(f"{name}: character.md exceeds {MAX_MD} bytes")
        text = md.read_text(encoding="utf-8")
        for h in HEADINGS:
            if h not in text:
                errors.append(f"{name}: character.md missing '{h}' section")
        m = STYLE_RE.search(text)
        if not m:
            errors.append(f"{name}: character.md missing a 'Style: <look>' line")
        else:
            declared_styles[name] = m.group(1)
        am = ALIASES_RE.search(text)
        if am:
            declared_aliases[name] = [a.strip() for a in am.group(1).split(",") if a.strip()]
        spec = section(text, "## Prompt spec")
        if spec and not re.search(r"^\s*>", spec, re.M):
            errors.append(f"{name}: '## Prompt spec' has no blockquoted paragraph "
                          f"(the CHARACTER-slot text must be a > quote)")
        if spec and "accent" not in spec.lower():
            errors.append(f"{name}: prompt spec never names the accent carrier — "
                          f"exactly one accent-colored part is structural; "
                          f"'accent' must appear in the spec")

    for png in d.glob("*.png"):
        b = png.read_bytes()
        if png.stat().st_size > MAX_PNG:
            errors.append(f"{name}: {png.name} exceeds {MAX_PNG} bytes")
        if b[:8] != PNG_MAGIC:
            errors.append(f"{name}: {png.name} is not a real PNG")
        else:
            w, h = png_size(b)
            if w and h and min(w, h) < MIN_PX:
                errors.append(f"{name}: {png.name} is {w}x{h} — short side under {MIN_PX}px")

idx_aliases = {}
try:
    idx = json.loads((ROOT / "index.json").read_text(encoding="utf-8"))
    entries = idx["packs"]
    listed = {p.get("name") for p in entries}
    actual = {d.name for d in packs}
    for missing in sorted(actual - listed):
        errors.append(f"index.json: no entry for pack {missing}")
    for stale in sorted(listed - actual):
        errors.append(f"index.json: entry for nonexistent pack {stale}")
    if len(listed) != len(entries):
        errors.append("index.json: duplicate pack names")
    for p in entries:
        pname = p.get("name", "?")
        for key in ("name", "author", "version", "description", "style"):
            if not p.get(key):
                errors.append(f"index.json: {pname}: missing {key}")
        if p.get("version") and not SEMVER.fullmatch(p["version"]):
            errors.append(f"index.json: {pname}: version {p['version']!r} is not semver")
        if p.get("description") and len(p["description"]) > MAX_DESC:
            errors.append(f"index.json: {pname}: description over {MAX_DESC} chars")
        style = p.get("style")
        if style and not KEBAB.fullmatch(style):
            errors.append(f"index.json: {pname}: style {style!r} is not kebab-case")
        elif style and style not in LOOKS:
            errors.append(f"index.json: {pname}: style {style!r} is not a bundled "
                          f"look — catalog packs must use one of: "
                          f"{', '.join(sorted(LOOKS))} (custom styles stay local "
                          f"until promoted into the skill's look library)")
        if style and pname in declared_styles and declared_styles[pname] != style:
            errors.append(f"index.json: {pname}: style {style!r} != character.md "
                          f"Style line {declared_styles[pname]!r}")
        if "aliases" in p:
            if not isinstance(p["aliases"], list) or not all(isinstance(a, str) for a in p["aliases"]):
                errors.append(f"index.json: {pname}: aliases must be a list of strings")
            else:
                idx_aliases[pname] = p["aliases"]
except Exception as e:  # malformed JSON, missing file, wrong shape
    errors.append(f"index.json: {e}")

# Aliases are selection keys like the pack name ("use ox" -> yoke), so they are
# validated like names: lowercase kebab-case, not reserved, globally unique, and
# never a pack name. The character.md Aliases: line and index.json aliases array
# must match — packs list reads the index, the installed pack reads character.md.
pack_names = {d.name for d in packs}
alias_owner = {}  # alias -> first pack that claimed it
for name in sorted(set(declared_aliases) | set(idx_aliases)):
    md_a, ix_a = declared_aliases.get(name, []), idx_aliases.get(name, [])
    if set(md_a) != set(ix_a):
        errors.append(f"{name}: character.md Aliases {md_a} != index.json aliases {ix_a}")
    for a in dict.fromkeys(md_a + ix_a):  # ordered union
        if not KEBAB.fullmatch(a):
            errors.append(f"{name}: alias {a!r} is not lowercase kebab-case")
        if a in RESERVED:
            errors.append(f"{name}: alias {a!r} is reserved (shipped character or look name)")
        if a in pack_names:
            errors.append(f"{name}: alias {a!r} collides with a pack name")
        if a in alias_owner and alias_owner[a] != name:
            errors.append(f"{name}: alias {a!r} already claimed by {alias_owner[a]}")
        alias_owner.setdefault(a, name)

if errors:
    print("\n".join(f"FAIL: {e}" for e in errors))
    sys.exit(1)
print(f"OK: {len(packs)} pack(s) valid")
