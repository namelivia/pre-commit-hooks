import argparse
import emoji
import re
from typing import Optional
from typing import Sequence
import os
import sys

if sys.platform.lower() == "win32":
    os.system("color")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check")
    parser.add_argument("--pattern", help="Pattern to check")
    parser.add_argument("--custom_message", help="Custom message to print")
    parser.add_argument(
        "--critical", help="If active the regex matching should block the commit",
    )
    args = parser.parse_args(argv)

    files_containing = []
    is_critical = args.critical is not None

    for filename in args.filenames:
        with open(filename, "rb") as f:
            line = f.read()
            files_containing.append(filename) if re.search(
                re.compile(args.pattern.encode()), line
            ) else None

    if files_containing:
        color = "\033[31m" if is_critical else "\033[33m"
        icon = (
            emoji.emojize(":no_entry:")
            if is_critical
            else emoji.emojize(":bulb:", use_aliases=True)
        )
        for file_contaning in files_containing:
            print(f"{color}{icon} {file_contaning}: {args.custom_message}\033[0m")
        if is_critical:
            return 1
    return 0


if __name__ == "__main__":
    exit(main())
