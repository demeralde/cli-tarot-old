import sys

from tarot.cli import CLI


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    cli = CLI()


if __name__ == "__main__":
    sys.exit(main())
