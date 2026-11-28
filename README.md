# Daily Parser

We will build a parser for an international standard every day until January 1st, 2027!  
However, the international standards are strictly limited to string-based formats.

## Rules
1. Zero-Dependency: No external libraries, and not even Python built-in libraries (`re`, `datetime`, `json`, `urllib`, etc.) are allowed for parsing logic. Parsing must be implemented using pure syntax and primitive data types (`str`, `int`, `list`, `dict`, etc.) only. *(Exception: `typing` and `dataclasses` are allowed solely for type annotations and structuring parsed results.)*
2. String Only: Only text-based international standards (RFC, ISO, ECMA, etc.) are covered—no binary formats.
3. 1 Day 1 Parser: Add support for one new standard parser every day from November 27th, 2026, to January 1st, 2027.

## Supported Standards
- [ ] Day 01 (2026-11-27): `Semantic Versioning 2.0.0`
- [ ] Day 02 (2026-11-28): `UUID (RFC 9562 / RFC 4122)`
- [ ] Day 03 (2026-11-29): `ISBN-13 (ISO 2108)`
- [ ] Day 04 (2026-11-30): `Base64 (RFC 4648)`
- [ ] Day 05 (2026-12-01): `Data URL (RFC 2397)`
- [ ] Day 06 (2026-12-02): `HTTP Date (RFC 9110)`
- [ ] Day 07 (2026-12-03): `HTTP/1.1 Message Head (RFC 9112)`
- [ ] Day 08 (2026-12-04): `URI / URL (RFC 3986)`
- [ ] Day 09 (2026-12-05): `JWT (RFC 7519)`
- [ ] Day 10 (2026-12-06): `CSV (RFC 4180)`
...

## Project Period
2026-11-27 ~ 2027-01-01