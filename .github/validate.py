#!/usr/bin/env python3
"""Validate pack structure for illo-characters. Stdlib only; run from anywhere."""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PACKS = ROOT / "packs"
REQUIRED = ("character.md", "reference.png", "preview.png")
HEADINGS = ("## Locked design", "## Prompt spec", "## Value rules")
MAX_MD = 16 * 1024
MAX_PNG = 3 * 1024 * 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

errors = []
packs = sorted(d for d in PACKS.iterdir() if d.is_dir()) if PACKS.is_dir() else []
if not packs:
    errors.append("packs/ is missing or empty")

for d in packs:
    name = d.name
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        errors.append(f"{name}: pack name is not lowercase kebab-case")
    for f in REQUIRED:
        if not (d / f).is_file():
            errors.append(f"{name}: missing {f}")
    for f in d.iterdir():
        if f.name.startswith(".") or f.suffix not in (".md", ".png"):
            errors.append(f"{name}: disallowed file {f.name} (only .md/.png)")
    md = d / "character.md"
    if md.is_file():
        if md.stat().st_size > MAX_MD:
            errors.append(f"{name}: character.md exceeds {MAX_MD} bytes")
        text = md.read_text(encoding="utf-8")
        for h in HEADINGS:
            if h not in text:
                errors.append(f"{name}: character.md missing '{h}' section")
    for png in d.glob("*.png"):
        if png.stat().st_size > MAX_PNG:
            errors.append(f"{name}: {png.name} exceeds {MAX_PNG} bytes")
        if png.read_bytes()[:8] != PNG_MAGIC:
            errors.append(f"{name}: {png.name} is not a real PNG")

try:
    idx = json.loads((ROOT / "index.json").read_text(encoding="utf-8"))
    entries = idx["packs"]
    listed = {p.get("name") for p in entries}
    actual = {d.name for d in packs}
    for missing in sorted(actual - listed):
        errors.append(f"index.json: no entry for pack {missing}")
    for stale in sorted(listed - actual):
        errors.append(f"index.json: entry for nonexistent pack {stale}")
    for p in entries:
        for key in ("name", "author", "version", "description"):
            if not p.get(key):
                errors.append(f"index.json: {p.get('name', '?')}: missing {key}")
except Exception as e:  # malformed JSON, missing file, wrong shape
    errors.append(f"index.json: {e}")

if errors:
    print("\n".join(f"FAIL: {e}" for e in errors))
    sys.exit(1)
print(f"OK: {len(packs)} pack(s) valid")
