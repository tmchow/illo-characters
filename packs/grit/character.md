# Grit — character pack

A pixel-built tardigrade — the pudgy microscopic animal that survives
anything. The name is the temperament: grit is whatever is still standing
when the meteors stop.

Credit: **Grit by Trevin Chow**.

Style: **pixel**

## Locked design

- **Body**: one loaf-shaped pudgy mass with a blunt rounded front — a
  single smooth-silhouetted pixel loaf, built from hard square pixels with
  a 1-pixel stair-stepped outline. Nothing breaks the outline.
- **Face**: two simple square pixel dot eyes directly on the blunt front.
  Completely blank, deadpan, neutral — **no eyebrows, no mouth, ever**.
- **Legs**: exactly **four** stubby legs (the house anatomy is just the
  real animal) — soft pixel stubs, no claws, no toes, no feet detail.
- **Accent carrier**: the short blunt **snout-tube** on the front of the
  loaf — a small cylinder on the loaf, the only accent-colored part.
- Cuteness comes from proportion and roundness, never from added parts.
- Never add: the real tardigrade's other four legs (always four, never
  eight), body segmentation rings, wrinkles or folds, claws, a mouth
  opening on the snout-tube, antennae, teeth, tools, hats, clothing,
  accessories — and never a smooth anti-aliased rendering: the mascot is
  pixel-built like everything else in the image.

## Prompt spec

> the recurring mascot — a pudgy loaf-shaped tardigrade (water bear): one
> rounded pixel loaf with a blunt rounded front, exactly four stubby legs
> (never eight, no claws), two simple square dot eyes, blank deadpan (no
> eyebrows, no mouth); the ONLY accent-colored part is the short blunt
> snout-tube on the front of the loaf (state the accent hue in words next
> to its hex — accent colors drift otherwise). No body segments, no rings,
> no wrinkles, no extra parts. It MUST perform the move, not decorate. The
> mascot itself is built from visible square pixels with a 1-pixel
> stair-stepped outline on the same pixel grid as every other shape — it
> must NOT be smoother than the rest of the image. {value rule: on a light
> ground the body fills with the background color and carries a
> stair-stepped ink outline with ink-pixel eyes; on a dark ground the body
> fills with the mid color and the eyes go background-colored; the
> snout-tube stays accent in every palette}

## Value rules

Pixel quantizes every image to exactly 4 colors (see the style's palette
mapping: background ← paper, ink ← structure, mid ← structure hue at ~60%
lightness, accent ← palette accent):

- The body fills with the **background** color and reads through its
  1-pixel stair-stepped **ink** outline; eyes are ink pixels. On a dark
  ground the body fills with the **mid** color instead, eyes
  background-colored, so the loaf always separates from the ground.
- Legs are part of the body — same fill, same outline, never mid-colored
  separately, never accent.
- The snout-tube takes the palette **accent** in every palette — always
  name the accent hue in words beside the hex (classic default: magenta
  `#e0359a`); accent colors drift otherwise.
- Classic default palette: background `#f2ead8`, ink `#1c1a17`, mid
  `#a89c88`, accent magenta `#e0359a`.

## Personality

Has survived worse and does not bring it up. The character for resilience
and fault tolerance — surviving outages, chaos testing, graceful
degradation, disaster recovery, "still up after everything". Boss prevents
the attack, anvil takes the feedback; grit endures the failure and files
no complaint.
