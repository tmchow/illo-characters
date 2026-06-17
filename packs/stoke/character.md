# Stoke — character pack

A vacuum tube kept warm. The name is the job — stoking the filament so the
answer comes back hot instead of from a cold start.

Credit: **Stoke by Trevin Chow**.

Style: **phosphor**
Aliases: vacuum-tube, tube, valve

## Locked design

- **Body**: one tall rounded-top cylinder with the proportions of a fat
  thermos, topped by a small flat metal cap — a single upright column,
  completely different from a round screw-in bulb.
- **Base**: a wide solid socket puck — a plain flat disc it stands on
  directly. **No pins, no screw threads, ever.**
- **Glow core**: a single soft vertical core of warm light up the middle of
  the body, like a heated filament — one smooth column of glow, never drawn
  wiring, coils, or zigzag filament lines.
- **Face**: two simple dot eyes directly on the cylinder, blank deadpan —
  **no eyebrows, no mouth, ever**.
- **Arms**: small stubby arms off the cylinder sides; it stands on its
  socket puck, no separate legs.
- **Accent carrier**: the filament-glow core — the only accent-colored part.
  Bright when warm, dark when cold.
- Cuteness comes from proportion and roundness, never from added parts.
- Never add: drawn filament wires, coils, or zigzags inside the core; socket
  pins or a threaded screw-in base; bulb roundness (it is a column, not a
  light bulb); glass reflections or highlights; panels, seams, bolts,
  gauges, vents; a monitor bezel; mouth, eyebrows, hats, clothing,
  accessories.

## Prompt spec

> the recurring mascot — a vacuum tube: one tall rounded-top cylinder with
> the proportions of a fat thermos, a small flat metal cap on top, standing
> on a wide solid socket puck (a plain flat disc base, NO pins, NO screw
> threads — a column, not a round light bulb); a single soft vertical core
> of warm light glows up the middle of the body like a heated filament —
> one smooth column of glow, never drawn wiring or coils; two simple dot
> eyes on the cylinder, blank deadpan (no eyebrows, no mouth), small stubby
> arms off the cylinder sides; the ONLY accent-colored part is the
> filament-glow core (state the accent hue in words next to the hex — it is
> warm amber, never green). It MUST perform the move, not decorate. {value
> rule: drawn in the same crisp glowing trace as everything else, eyes as
> solid trace-color dots, the filament core glowing in the accent color —
> never a solid filled sprite}

## Value rules

Phosphor inverts the riso grammar — dark ground, luminous line (see the
style's palette mapping):

- The body is **trace only** — cylinder, cap, socket puck, and arms drawn
  as crisp glowing strokes of one even weight on the near-black screen,
  never a solid filled sprite. The spec's "smoky dark glass" is the dark
  screen itself showing through the outline.
- Eyes are solid glowing dots in the **trace color**.
- The filament core is the single accent element — one soft vertical bar of
  **warm amber** glow. Classic palette: screen `#0b100d`, trace green
  `#3fe88e`, accent amber `#ffb648`. Always name the accent hue in words
  beside the hex — on a green-trace screen the core drifts green otherwise.
- Warm = the core glows bright amber; cold = the core goes dark and only
  the outline remains.
- Accent discipline: the core plus at most 1–2 scene elements; nothing else
  takes amber.

## Personality

Warm and ready before you ask — glows quietly, never quite goes cold. Good
for readiness, staying warm for next time, and caching and warm starts.
