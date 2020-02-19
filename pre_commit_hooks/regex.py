import argparse
import re
from typing import Optional
from typing import Sequence
import os
import sys

if sys.platform.lower() == "win32":
    os.system('color')


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    parser.add_argument(
        '--expressions',
        nargs='*',
        help='Expressions to check',
        default=[]
    )
    parser.add_argument('--custom_message', help='Custom message to print')
    parser.add_argument(
        '--critical',
        help='If active the regex matching should block the commit',
        default=False
    )
    args = parser.parse_args(argv)

    files_containing = []

    for filename in args.filenames:
        with open(filename, 'rb') as f:
            line = f.read()
            files_containing.append(filename) if any(
                re.search(re.compile(expression.encode()), line)
                for expression in args.expressions
            ) else None

    if files_containing:
        color = '\033[31m' if args.critical else '\033[33m'
        icon = '\U000026A0' if args.critical else '\U00002604'
        for file_contaning in files_containing:
            print(
                f'{color}{icon}{file_contaning}: {args.custom_message}\033[0m'
            )
        if (args.critical):
            return 1
    else:
        return 0


if __name__ == '__main__':
    exit(main())
