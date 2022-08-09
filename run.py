from importlib import import_module
from inspect import getmembers
from sys import argv


def main():
    if argv[1] in ["-p", "--problem"]:
        problem = import_module(f"problem_{argv[2]}", ".")
        problem.run()


if __name__ == "__main__":
    main()
