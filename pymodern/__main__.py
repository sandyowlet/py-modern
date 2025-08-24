import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import cast

import yaml
from copier import run_copy

SOURCE_DIR = Path(__file__).parent.parent


@dataclass
class PymodernArgs:
    project_dir: Path
    answers_file: Path | None = None


parser = argparse.ArgumentParser()
parser.add_argument(
    "-p",
    "--project-dir",
    type=Path,
    default=Path.cwd(),
    required=False,
)
parser.add_argument("-a", "--answers-file", type=Path, default=None, required=False)


def main() -> None:
    args = parser.parse_args()
    args = cast("PymodernArgs", args)

    if args.answers_file is not None:
        with args.answers_file.open() as f:
            answers = yaml.safe_load(f)
    else:
        answers = None

    run_copy(
        str(SOURCE_DIR),
        str(args.project_dir),
        data=answers,
    )


if __name__ == "__main__":
    main()
