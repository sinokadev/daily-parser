from dataclasses import dataclass
from .errors import SpecViolationError

HEX_CHARS = set("0123456789abcdefABCDEF")
NIL_UUID = "00000000-0000-0000-0000-000000000000"
MAX_UUID = "ffffffff-ffff-ffff-ffff-ffffffffffff"


@dataclass
class UUID:
  canonical: str
  version: int | None
  variant: str
  bytes: bytes
  is_nil: bool
  is_max: bool
  timestamp_ms: int | None


def uuid(_uuid: str) -> UUID:
  if len(_uuid) != 36:
    raise SpecViolationError("Invalid UUID length")

  parts = _uuid.split("-")
  if [len(p) for p in parts] != [8, 4, 4, 4, 12]:
    raise SpecViolationError("Invalid UUID format")

  hex_str = "".join(parts)
  if not all(c in HEX_CHARS for c in hex_str):
    raise SpecViolationError("Invalid character in UUID")

  canonical = _uuid.lower()
  raw_bytes = bytes.fromhex(hex_str)

  if canonical == NIL_UUID:
    return UUID(
        canonical=canonical,
        version=None,
        variant="Nil",
        bytes=raw_bytes,
        is_nil=True,
        is_max=False,
        timestamp_ms=None,
    )

  if canonical == MAX_UUID:
    return UUID(
        canonical=canonical,
        version=None,
        variant="Max",
        bytes=raw_bytes,
        is_nil=False,
        is_max=True,
        timestamp_ms=None,
    )

  if (raw_bytes[8] & 0xC0) != 0x80:
    raise SpecViolationError("Invalid UUID variant")

  version = raw_bytes[6] >> 4
  if not (1 <= version <= 8):
    raise SpecViolationError("Invalid UUID version")

  timestamp_ms = int.from_bytes(raw_bytes[0:6], "big") if version == 7 else None

  return UUID(
      canonical=canonical,
      version=version,
      variant="RFC 9562",
      bytes=raw_bytes,
      is_nil=False,
      is_max=False,
      timestamp_ms=timestamp_ms,
  )