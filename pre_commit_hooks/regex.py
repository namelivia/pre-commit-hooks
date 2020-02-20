import argparse
import emoji
import re
from typing import Optional
from typing import Sequence
import os
import sys

if sys.platform.lower() == "win32":
    os.system("color")


def _get_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check")
    parser.add_argument("--pattern", help="Pattern to check")
    parser.add_argument("--message", help="Message to print when pattern is present")
    parser.add_argument(
        "--critical",
        help="If present when the patterin is present the commit is blocked",
        action="store_true",
    )
    return parser.parse_args(argv)


def _get_matching_files(expression, filenames):
    result = []
    for filename in filenames:
        with open(filename, "rb") as f:
            line = f.read()
            if re.search(expression, line):
                result.append(filename)
    return result


def _report_results(matching_files, critical, message):
    color = "\033[31m" if critical else "\033[33m"
    icon = (
        emoji.emojize(":no_entry:") if critical else emoji.emojize(":bulb:", use_aliases=True)
    )
    for matching_file in matching_files:
        print(f"{color}{icon} {matching_file}: {message}\033[0m")


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _get_arguments(argv)
    expression = re.compile(args.pattern.encode())
    matching_files = _get_matching_files(expression, args.filenames)

    if matching_files:
        _report_results(matching_files, args.critical, args.message)
        if args.critical:
            return 1
    return 0


if __name__ == "__main__":
    exit(main())
