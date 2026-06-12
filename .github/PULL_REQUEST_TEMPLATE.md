## <Name> — <one-line description>

By <author>. <One sentence: the design and what carries the accent.>

| Model sheet | In action |
|---|---|
| ![model sheet](https://raw.githubusercontent.com/OWNER/illo-characters/BRANCH/packs/NAME/reference.png) | ![preview](https://raw.githubusercontent.com/OWNER/illo-characters/BRANCH/packs/NAME/preview.png) |

<!-- Replace OWNER (your fork's user), BRANCH, and NAME above so both images
render — reviewers judge the preview scene at a glance. If your design
diverges from the house family look (a mouth, a different body plan, a body
built from a material), add one line saying what diverges and why it's
deliberate — divergent packs get the closer review. -->

### Checklist

- [ ] `packs/<name>/` has `character.md`, `reference.png`, `preview.png` (real PNGs — check with `file`)
- [ ] `index.json` entry added: `name`, `author`, `version`, `description`, `style` (a bundled look)
- [ ] README catalog table row added
- [ ] `python3 .github/validate.py` passes locally
