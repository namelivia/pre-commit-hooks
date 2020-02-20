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
        "--critical",
        help="If present the regex matching should block the commit",
        action="store_true",
    )
    args = parser.parse_args(argv)

    files_containing = []

    for filename in args.filenames:
        with open(filename, "rb") as f:
            line = f.read()
            if re.search(
                re.compile(args.pattern.encode()),
                line
            ):
                files_containing.append(filename)

    if files_containing:
        color = "\033[31m" if args.critical else "\033[33m"
        icon = (
            emoji.emojize(":no_entry:")
            if args.critical
            else emoji.emojize(":bulb:", use_aliases=True)
        )
        for file_contaning in files_containing:
            print(f"{color}{icon} {file_contaning}: {args.custom_message}\033[0m")
        if args.critical:
            return 1
    return 0


if __name__ == "__main__":
    exit(main())
