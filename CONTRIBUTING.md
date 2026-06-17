# Contributing a character pack

A pack is one folder: `packs/<name>/` with exactly these files.

## Pack format

| File | What it is |
|---|---|
| `character.md` | The written spec. Must contain the sections `## Locked design`, `## Prompt spec`, `## Value rules`, and a `Style: <look>` line naming one of the twelve bundled looks — riso, blueprint, woodcut, pixel, clay, manila, chalk, phosphor, enamel, gouache, felt, diorama (custom styles work locally but can't ship in catalog packs yet; add `## Personality` and a credit line as you like). Lead the description and personality with what the character *is and does* — keep any engineering use-case as one lens at the end, not the headline. Optionally an `Aliases:` line — comma-separated subject synonyms (`Aliases: ox, zebu`) so users can summon the pack by what it is ("use ox" → `yoke`); add it when the name doesn't plainly read off the subject. The prompt spec is one blockquoted paragraph that drops into illo's CHARACTER prompt slot. |
| `reference.png` | The canonical model sheet — one clean, front-facing, full-body render on plain paper. This is the consistency anchor the skill passes as `--ref`. |
| `preview.png` | One *scene* render where the character performs an idea (load-bearing, not posing). This is the review artifact: a model sheet can hide a character that falls apart in scenes. |

Rules (CI-enforced by `.github/validate.py` on every PR):

- `<name>` is lowercase kebab-case and **globally unique** — `index.json`
  here is the ecosystem's name registry ("use <name>" is how agents select
  characters). Reserved names: `blot`, `illo`, and the ten look names
  (`riso`, `blueprint`, `woodcut`, `pixel`, `clay`, `manila`, `chalk`,
  `phosphor`, `enamel`, `gouache`). **Aliases are selection keys too** — each
  must be kebab-case, not reserved, not a pack name, and unique across all
  packs (CI enforces this).
- Only `.md` and `.png` files; `character.md` ≤ 16 KB; each PNG ≤ 3 MB.
- Add an entry to `index.json` (`name`, `author`, `version`, `description`,
  `style`, plus optional `aliases` mirroring the `Aliases:` line) and a row
  to the README catalog table in the same PR.
- One pack, one look. A variant of an existing character in another style is
  its own pack, named `<name>-<style>` (e.g. `blip-woodcut`).
- CI also checks definition content: the prompt spec is a blockquote and
  names the one accent carrier; the `Style:` line matches the index `style`
  field and is a bundled look; the `Aliases:` line matches the index
  `aliases` array (when present); versions are semver; descriptions ≤ 200
  chars; images are ≥ 512 px on the short side and have a README catalog row.

## Design bar

Characters follow illo's character rules (see
[`references/character.md`](https://github.com/tmchow/illo-skill/blob/main/skills/illo/references/character.md)
in the skill). The **structural rules** bind every pack: one simple
silhouette, a locked exactly-specified face, exactly ONE accent-carrying
part, and nothing a render can improvise — every part, accessory, or body
treatment must be named in the locked design. The **house family look** (two
dot eyes, blank deadpan, stubby limbs) is the default the builder steers
toward, not a requirement: a character with a mouth, a different body plan,
or a body built from a material is welcome when the divergence is deliberate
and locked in render-checkable terms — expect a higher review bar, judged on
your preview render ("does it still read as illo in a scene?"). Characters
must also be distinct from existing packs and from visual clichés. The
easiest way to meet the bar is to build the pack with the skill's character
builder — it pressure-tests the concept and generates the model sheet for
you.

## Publishing

The illo skill can do this for you ("publish my character") — it forks this
repo, adds your pack + index entry, and opens a PR whose description embeds
your `reference.png` and `preview.png` so review takes one glance.

Manually: fork → add `packs/<name>/` + the `index.json` entry + the README
row → run `python3 .github/validate.py` → open a PR. Embed your two images in
the PR body via their raw URLs on your branch:

```text
![model sheet](https://raw.githubusercontent.com/<you>/illo-characters/<branch>/packs/<name>/reference.png)
![preview](https://raw.githubusercontent.com/<you>/illo-characters/<branch>/packs/<name>/preview.png)
```

## Review & licensing

Maintainers review for the design bar, name collisions, and content (packs
are public; keep them safe-for-work, no third-party IP you don't own). By
submitting you license your pack under the repo's MIT license; you keep
authorship and the credit line in `character.md`.
