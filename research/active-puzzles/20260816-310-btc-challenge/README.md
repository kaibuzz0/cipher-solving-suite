# 310 BTC Challenge

- **Case ID:** `20260816-310-btc-challenge`
- **Type:** `crypto-puzzle`
- **Status:** `triaged`
- **Source:** legacy repository research
- **Owner:** unclaimed

## Evidence map

| Repository path | Role | Current decision |
|---|---|---|
| `310_challenge.png` | Primary challenge image | **PRIMARY EVIDENCE — DO NOT MOVE YET** |
| `alpha_lsb.bin` | Alpha LSB extraction | Generated output; link then organize |
| `alpha_pattern.bin` | Alpha pattern extraction | Generated output; link then organize |
| `alpha_2bit.bin` | Alpha 2-bit extraction | Generated output; link then organize |
| `alpha_row310.bin` | Row-310 alpha extraction | Generated output; link then organize |
| `bitplanes/` | RGB bitplane analysis | Generated outputs; duplicate review required |
| `alpha_extract.py` | Reproduction script | Case tool/source code |
| `analyze_310.py` | Analysis script | Case tool/source code |

## Known reproduction relationships

`alpha_extract.py` explicitly writes the four `alpha_*.bin` outputs. Its current `main()` contains a legacy absolute input path (`/root/310_btc_challenge/310_challenge.png`), so that path should be repaired before claiming clean reproducibility.

`analyze_310.py` performs image/color/LSB analysis and writes channel/difference outputs when its quick-analysis path is used.

## Duplicate observation

The repository tree proves multiple `bitplanes/bitplane_g_*.png` and `bitplanes/bitplane_b_*.png` files share the same Git blob SHA for corresponding bit indices. These are byte-identical duplicate groups and must not be auto-deleted. The migration review chooses a canonical retained representation only after references are checked.

## Next action

1. Preserve and hash the primary image in place.
2. Repair/parameterize the legacy absolute path in `alpha_extract.py` before relying on reproduction.
3. Generate the artifact inventory and capture all duplicate groups.
4. Link the generated outputs to this case in inventory metadata.
5. Move only reviewed generated outputs into this case; do not move/delete the primary image yet.
