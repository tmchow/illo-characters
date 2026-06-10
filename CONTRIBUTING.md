# Contributing a character pack

A pack is one folder: `packs/<name>/` with exactly these files.

## Pack format

| File | What it is |
|---|---|
| `character.md` | The written spec. Must contain the sections `## Locked design`, `## Prompt spec`, `## Value rules`, and a `Style: <look>` line (the pack's one look — riso, blueprint, woodcut, pixel, or a custom style; add `## Personality` and a credit line as you like). The prompt spec is one blockquoted paragraph that drops into illo's CHARACTER prompt slot. |
| `reference.png` | The canonical model sheet — one clean, front-facing, full-body render on plain paper. This is the consistency anchor the skill passes as `--ref`. |
| `preview.png` | One *scene* render where the character performs an idea (load-bearing, not posing). This is the review artifact: a model sheet can hide a character that falls apart in scenes. |

Rules (CI-enforced by `.github/validate.py`):

- `<name>` is lowercase kebab-case and unique in `packs/`.
- Only `.md` and `.png` files; `character.md` ≤ 16 KB; each PNG ≤ 3 MB.
- Add an entry to `index.json` (`name`, `author`, `version`, `description`,
  `style`) and a row to the README catalog table in the same PR.
- One pack, one look. A variant of an existing character in another style is
  its own pack, named `<name>-<style>` (e.g. `blip-woodcut`).

## Design bar

Characters follow illo's character rules (see
[`references/character.md`](https://github.com/tmchow/agent-skills/blob/main/illo/references/character.md)
in the skill): one simple silhouette, two dot eyes, blank deadpan, stubby
limbs, exactly ONE accent-carrying part, no detail creep, distinct from
existing packs and from visual clichés. The easiest way to meet the bar is to
build the pack with the skill's character builder — it pressure-tests the
concept and generates the model sheet for you.

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
