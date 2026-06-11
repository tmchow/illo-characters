# Dice — character pack

A single softly rounded white die with one pip, built from pixels. The name
reads straight off the form — the cube you roll when the outcome could land
either way.

Credit: **Dice by Trevin Chow**.

Style: **pixel**

## Locked design

- **Body**: one plump, softly rounded cube — a single white die, slightly
  squashed, with marshmallow corners, standing upright on one face. It reads
  as a square blob at thumbnail size; in pixel rendering the soft corners
  become short stair-stepped bevels, never smooth curves.
- **Face**: two simple dot eyes on the front face. Completely blank,
  deadpan, neutral — **no eyebrows, no mouth, ever**.
- **Limbs**: small stubby arms at the sides and small stubby legs below —
  enough to brace, steady, and carry; no hands, no fingers spelled out.
- **Accent carrier**: the **single round pip on its top face** — the only
  accent-colored part. Every other face of the die is completely blank: no
  other pips, no numerals, ever.
- Cuteness comes from proportion and squash, never from added parts.
- Never add: extra pips on any face, numerals or letters on the body, a
  second die or dice pair, casino chips/cards/iconography, gloss highlights,
  gradients, anti-aliased or smooth curved edges (the body is pixel-built and
  stair-stepped like everything else), eyebrows, mouth, hats, clothing,
  accessories.

## Prompt spec

> the recurring mascot — a single plump softly-rounded white die, slightly
> squashed, a marshmallow-cornered cube standing upright on one face with its
> top face just visible; two simple dot eyes on the front face, blank deadpan
> (no eyebrows, no mouth), small stubby arms and legs; the ONLY
> accent-colored part is the single round pip centered on its TOP face (state
> the accent hue in words next to the hex — accent colors drift otherwise),
> and every other face is completely blank — no other pips, no numerals,
> ever. It MUST perform the move, not decorate. The mascot itself is built
> from visible square pixels with a stair-stepped outline, exactly like every
> other shape — it must NOT be smoother than the rest of the image. {value
> rule: the body is filled with the lightest of the four quantized colors
> (the background tone in the classic palette) with a stair-stepped ink
> outline; eyes are ink pixels; only the top-face pip takes the accent}

## Value rules

Pixel quantizes every scene to exactly 4 colors — background, ink, mid,
accent (see the style's palette mapping):

- The body fill is the **lightest of the four colors** — in the classic
  default palette that is the background cream `#f2ead8` — so the die always
  reads white, with a 1-pixel stair-stepped **ink** outline.
- Eyes are **ink** pixels on the front face.
- The single top-face pip takes the **accent** (classic default: magenta
  `#e0359a`). Always name the accent hue in words beside the hex — accent
  colors drift otherwise.
- The **mid** tone never appears on the character; it is reserved for
  secondary shapes and props.

## Personality

The house fatalist — accepts every outcome as the one it predicted, and is
never surprised when the re-run lands the other way. The character for
chance and nondeterminism: flaky tests, A/B experiments, bets and risky
rollouts, RNG, LLM output variance, and every "roll the dice" decision.
