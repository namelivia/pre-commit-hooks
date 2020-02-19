import argparse
from typing import Optional
from typing import Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    parser.add_argument('expressions', nargs='*', help='Expressions to check')
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
            content = f.read()
            if any(line in content for line in args.expressions):
                files_containing.append(filename)

    if files_containing:
        for file_contaning in files_containing:
            print(f'{file_contaning}: {args.custom_message}')
        if (args.critical):
            return 1
    else:
        return 0


if __name__ == '__main__':
    exit(main())
