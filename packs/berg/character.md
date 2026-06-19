# Berg — character pack

A small iceberg drawn as an engineering plan. The name reads straight off
the design — a berg shows the world its tip and keeps nine-tenths of itself
below the line, which is exactly the job.

Credit: **Berg by Trevin Chow**.

Style: **blueprint**
Cutout chroma: **magenta**
Aliases: iceberg, ice

## Locked design

- **Body**: one asymmetric low-peaked wedge of ice, like a worn shark
  tooth — wider than tall, built from a few large flat planes meeting at
  straight edges, with exactly **ONE** fixed off-center peak. The facet
  count is locked: a handful of big planes, never subdivided, render after
  render.
- **Face**: two simple dot eyes on the upper body, blank deadpan — **no
  eyebrows, no mouth, ever**.
- **Limbs**: small stubby arms at the sides; no legs — the wedge rests on
  its wide flat base (and floats in scenes).
- **Accent carrier**: the **peak-cap** — the small cap of ice at the very
  top of its single peak, the famous visible ten percent. The only
  accent-colored part.
- The dashed waterline belongs to **scenes**, not the body: in scenes a
  dashed line crosses the berg so its bulk reads as submerged; the model
  sheet shows the whole berg, no waterline.
- Never add: extra peaks, multiplied or subdivided facets, cracks or
  crevasse lines, internal hatching or shading on the planes, blue fill,
  snow texture, jagged saw-tooth edges, sea props stuck to the body,
  eyebrows, mouth, teeth, hats, clothing, accessories.

## Prompt spec

> the recurring mascot — a small iceberg: one asymmetric low-peaked wedge
> of ice like a worn shark tooth, wider than tall, built from a few large
> flat planes with straight edges and exactly ONE fixed off-center peak
> (never more facets, never more peaks), two simple dot eyes, blank deadpan
> (no eyebrows, no mouth), small stubby arms and no legs; the ONLY
> accent-colored part is the peak-cap at the very top of its single peak
> (state the accent hue in words next to the hex — accent colors drift
> otherwise). It MUST perform the move — floating at the line, propping,
> bearing the load on its hidden bulk — not decorate the scene. Drawn in
> the same white construction line as everything else, no fill, eyes as
> solid line-color dots, the peak-cap filled with the accent color. {value
> rule: on the deep blueprint ground the body is open line-color
> construction linework with zero fill and zero shading; eyes are solid
> line-color dots; only the peak-cap carries the accent}

## Value rules

Blueprint inverts the usual value logic — dark ground, light line — so the
dark/light body rules collapse to line-on-ground (see the style's palette
mapping):

- **Body**: open construction linework in the line color (classic
  `#f4f8ff`) on the blueprint ground (classic `#193a8c`). The planes are
  never filled or shaded — bulk reads through line, not tone.
- **Eyes**: solid dots in the line color.
- **Accent**: the peak-cap is the one filled part, in the palette accent —
  classic warm orange `#ff7a1a`. Always name the accent hue in words
  beside the hex; if a custom palette's accent is cool and vanishes
  against the ground, warm it by hue rotation toward orange per the style
  mapping.
- **Waterline**: in scenes, the dashed waterline and any submerged dashed
  structure are drawn in the line color like every other hidden edge —
  never in the accent.

## Personality

Calm on top, with a great deal more underneath that it doesn't advertise.
Good for hidden depth, the part you can't see yet, and estimates and hidden
complexity.
