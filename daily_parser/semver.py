from .errors import SpecViolationError
from dataclasses import dataclass

@dataclass
class SemVer:
    major: int
    minor: int
    patch: int
    prerelease: list[str | int]
    build: list[str]


ALLOWED_CHARS = set("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-")


def semver(_version: str) -> SemVer:
    if "+" in _version:
        version, build_raw = _version.split("+", 1)
        if "+" in build_raw:
            raise SpecViolationError("Multiple '+' in version")
        builds = build_raw.split(".")
        for b in builds:
            if not b:
                raise SpecViolationError("Empty build identifier")
            if not all(c in ALLOWED_CHARS for c in b):
                raise SpecViolationError("Invalid character in build metadata")
    else:
        version = _version
        builds = []

    if "-" in version:
        ver_front, pre = version.split("-", 1)
        pres_raw = pre.split(".")
        pres: list[str | int] = []
        for i in pres_raw:
            if not i:
                raise SpecViolationError("Empty prerelease identifier")
            if not all(c in ALLOWED_CHARS for c in i):
                raise SpecViolationError("Invalid character in prerelease")
            if i.isascii() and i.isdigit():
                if len(i) > 1 and i.startswith("0"):
                    raise SpecViolationError("Number cannot start with 0")
                pres.append(int(i))
            else:
                pres.append(i)
    else:
        ver_front = version
        pres = []

    core_parts = ver_front.split(".")
    if len(core_parts) != 3:
        raise SpecViolationError("Version core must have 3 parts")

    core_nums: list[int] = []
    for part in core_parts:
        if not part or not (part.isascii() and part.isdigit()):
            raise SpecViolationError("Invalid core version number")
        if len(part) > 1 and part.startswith("0"):
            raise SpecViolationError("Core version number cannot start with 0")
        core_nums.append(int(part))

    major, minor, patch = core_nums

    return SemVer(
        major=major,
        minor=minor,
        patch=patch,
        prerelease=pres,
        build=builds,
    )