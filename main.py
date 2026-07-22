from argparse import ArgumentParser, Namespace

from utils import new_command, run_command, search_command


def parse_args() -> Namespace:
    parser = ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    new_parser = sub.add_parser("new", help="scaffold a new problem by id")
    new_parser.add_argument("id", help="id of a problem")
    new_parser.set_defaults(func=new_command)

    run_parser = sub.add_parser("run", help="run tests for a problem by id")
    run_parser.add_argument("id", help="id of a problem")
    run_parser.set_defaults(func=run_command)

    search_parser = sub.add_parser(
        "search", help="search a problem if it exists, by id"
    )
    search_parser.add_argument("id", help="id of a problem")
    search_parser.set_defaults(func=search_command)

    return parser.parse_args()


def main():
    args = parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
