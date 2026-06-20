#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert Private Use Area (PUA) characters in all Markdown files to their
standard Unicode (decomposed/combining) equivalents.

Usage:
    python fix_pua.py [root_dir]

If no root_dir is given, the current directory is used. The script edits the
.md files in place and, at the end, reports any PUA characters that remain
(i.e. that are not covered by the mapping below) so they can be handled.
"""

import os
import sys
import unicodedata

# Mapping from PUA code point -> standard text (may contain combining marks).
PUA_MAP = {
    0xE000: "Ą́", 0xE001: "ą́", 0xE002: "Ą̃", 0xE003: "ą̃",
    0xE004: "Ę́", 0xE005: "ę́", 0xE006: "Ę̃", 0xE007: "ę̃",
    0xE008: "Ė́", 0xE009: "ė́", 0xE00A: "Ė̃", 0xE00B: "ė̃",
    0xE00C: "i̇̀", 0xE00D: "i̇́", 0xE00E: "i̇̃",
    0xE00F: "Į̇́", 0xE010: "į̇́",
    0xE011: "Į̇̃", 0xE012: "į̇̃",
    0xE013: "J̃", 0xE014: "j̇̃",
    0xE015: "L̃", 0xE016: "l̃",
    0xE017: "M̃", 0xE018: "m̃",
    0xE019: "R̃", 0xE01A: "r̃",
    0xE01B: "Ų́", 0xE01C: "ų́", 0xE01D: "Ų̃", 0xE01E: "ų̃",
    0xE01F: "Ū́", 0xE020: "ū́", 0xE021: "Ū̃", 0xE022: "ū̃",
}

# Translation table for str.translate(): maps code point -> replacement string.
TRANSLATION = {cp: repl for cp, repl in PUA_MAP.items()}


def is_pua(cp):
    """Return True if the code point lies in any Unicode Private Use Area."""
    return (
        0xE000 <= cp <= 0xF8FF              # BMP PUA
        or 0xF0000 <= cp <= 0xFFFFD         # Supplementary PUA-A
        or 0x100000 <= cp <= 0x10FFFD       # Supplementary PUA-B
    )


def find_md_files(root):
    """Yield the path of every .md file under root."""
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            if name.lower().endswith(".md"):
                yield os.path.join(dirpath, name)


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."

    changed_files = 0
    # remaining[code_point] = total count of that uncovered PUA char
    remaining = {}
    # remaining_locations[code_point] = set of file paths where it appears
    remaining_locations = {}

    for path in find_md_files(root):
        with open(path, encoding="utf-8") as f:
            text = f.read()

        new_text = text.translate(TRANSLATION)

        if new_text != text:
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(new_text)
            changed_files += 1

        # After conversion, look for any PUA characters still left over.
        for ch in new_text:
            cp = ord(ch)
            if is_pua(cp):
                remaining[cp] = remaining.get(cp, 0) + 1
                remaining_locations.setdefault(cp, set()).add(path)

    # ---- Report ----
    print("Converted PUA characters in {} file(s).".format(changed_files))

    if not remaining:
        print("No remaining PUA characters found.")
        return

    print("\nWARNING: {} uncovered PUA code point(s) still present:".format(len(remaining)))
    for cp in sorted(remaining):
        try:
            name = unicodedata.name(chr(cp))
        except ValueError:
            name = "<no Unicode name>"
        files = ", ".join(sorted(remaining_locations[cp]))
        print("  U+{:04X}  x{}  ({})  in: {}".format(cp, remaining[cp], name, files))


if __name__ == "__main__":
    main()
