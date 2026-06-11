# Sift — character pack

A footed colander. The name is the job — sift lets the noise fall straight
through its holes and walks away with the few things that matter.

Credit: **Sift by Trevin Chow**.

Style: **pixel**

## Locked design

- **Body**: one wide shallow bowl — a footed colander, wider than tall, the
  contour a single clean arc that reads at thumbnail size.
- **Holes**: a sparse FIXED grid of punched dot-holes inside the belly only —
  single structure-ink pixel dots, about three short rows, always inside the
  outline. The holes ARE pixels; they never touch the rim, feet, or contour.
- **Face**: two simple structure-ink dot eyes on the upper bowl, completely
  blank and deadpan — no eyebrows, no mouth, ever.
- **Rolled rim**: one continuous rolled band around the bowl's lip — the
  **accent carrier** and the only accent-colored part. The holes stay
  structure-tone, never accent.
- Small stubby arms at the sides and two stubby feet below.
- Everything, including the mascot, is built from visible square pixels with
  a stair-stepped outline — nothing about it is smooth.
- Never add: handles, a dense hole field, holes on the rim or feet, mesh or
  wire texture, steam, pasta or any food, a pedestal stem, mouth, eyebrows,
  accent-colored or highlighted holes, smooth anti-aliased curves.

## Prompt spec

> the recurring mascot — a footed colander: one wide shallow bowl body,
> wider than tall, with a rolled rim band around its lip and a sparse FIXED
> grid of punched dot-holes inside its belly (single structure-ink pixel
> dots, about three short rows, never dense, never on the rim or feet), two
> simple structure-ink dot eyes on the upper bowl, blank deadpan (no
> eyebrows, no mouth), small stubby arms and two stubby feet — no handles,
> no steam, no food; the rolled rim band is the ONLY accent-colored part
> (state the accent hue in words next to the hex — it drifts otherwise),
> and the holes stay structure-ink, never accent. It MUST perform the move,
> not decorate. The mascot itself is built from visible square pixels with a
> stair-stepped outline, exactly like every other shape — it must NOT be
> smoother than the rest of the image. {value rule: on the light pixel
> ground the bowl is light/paper-tone with a 1-pixel structure-ink
> stair-stepped outline, structure-ink eyes and holes; only the rolled rim
> takes the accent}

## Value rules

Pixel quantizes every scene to exactly 4 colors (background, ink, mid,
accent — see the style's palette mapping); sift maps onto them like this:

- **Bowl, arms, feet**: light — the background/paper tone — with a 1-pixel
  structure-ink stair-stepped outline, per the house light-palette rule.
- **Eyes and holes**: structure-ink pixel dots. The holes are part of the
  drawing's pixel grid, never highlights, never accent, never multiplied.
- **Rolled rim**: the palette accent, as one continuous band. Always name
  the accent hue in words beside the hex — accent colors drift otherwise.
- The mid tone belongs to secondary scene shapes, not to the character.
- On a dark-ground variant: the bowl stays the light tone against the
  ground, eyes and holes stay structure-ink, the rim stays accent.

## Personality

The triage desk that never panics — lets almost everything go, keeps
exactly what matters, and feels no need to explain the ratio. The character
for filtering and triage: signal vs noise, alert fatigue, inbox zero,
"most of this doesn't matter — these three do."
