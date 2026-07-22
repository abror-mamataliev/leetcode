import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROBLEMS_DIR = ROOT / "problems"
TEMPLATES_DIR = ROOT / "templates"


def find_problem(problem_id: str) -> Path:
    folder = PROBLEMS_DIR / problem_id
    if not folder.exists():
        print(f"Error: {folder} doesn't exist", file=sys.stderr)
        sys.exit(1)

    return folder


def new_command(args):
    problem_id = args.id
    folder = PROBLEMS_DIR / problem_id
    if folder.exists():
        print(f"Error: {folder} already exists", file=sys.stderr)
        sys.exit(1)

    folder.mkdir(parents=True)

    for file in ["solution.py", "test_solution.py"]:
        template = (TEMPLATES_DIR / f"{file}.tmpl").read_text()
        (folder / file).write_text(template)

    print(f"Created {folder}")


def run_command(args):
    problem_folder = find_problem(args.id)
    result = subprocess.run([sys.executable, "-m", "pytest", str(problem_folder), "-v"])
    sys.exit(result.returncode)


def search_command(args):
    problem_folder = find_problem(args.id)
    solution = (problem_folder / "solution.py").read_text()
    print(solution)
