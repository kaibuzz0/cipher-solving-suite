# Notes — 310 BTC Challenge

## 2026-08-16 — Legacy reconstruction

This case reconstructs the existing repository work around `310_challenge.png` rather than restarting analysis.

### Confirmed from code

- `alpha_extract.py` treats the image alpha channel as a possible steganographic data source and implements LSB, pattern, 2-bit, and row-310 extraction methods.
- The script explicitly saves `alpha_lsb.bin`, `alpha_pattern.bin`, `alpha_2bit.bin`, and `alpha_row310.bin`.
- `analyze_310.py` contains challenge-specific known-character and hex-grid hints and performs color, printable-data, per-channel LSB, channel extraction, and difference-image analysis.
- Existing `bitplanes/` files include real byte-identical groups across channels according to Git blob identities.

### Provenance gaps

- Original external challenge/source URL is not yet established in the structured case.
- The provenance of the checked-in `310_challenge.png` must therefore remain recorded as legacy repository evidence until an authoritative source is verified.
- No generated artifact should be interpreted as a successful solve merely because it exists.

### Safety of migration

The current task is repository organization and reproducibility. No cryptographic claim is being promoted by this migration pass.
