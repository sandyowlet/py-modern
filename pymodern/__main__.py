from pathlib import Path
from typing import Annotated

import typer
import yaml
from copier import run_copy

SOURCE_DIR = Path(__file__).parent.parent

app = typer.Typer()

DEFAULT_PROJECT_DIR = Path.cwd()


@app.command()
def lib(
    project_dir: Annotated[
        Path,
        typer.Option(
            "-p",
            "--path",
            help="Directory where the project will be created",
        ),
    ] = DEFAULT_PROJECT_DIR,
    answers_file: Annotated[
        Path | None,
        typer.Option(
            "-a",
            "--answers",
            help="YAML file containing answers for template questions",
        ),
    ] = None,
) -> None:
    """Create a new Python library project."""
    if answers_file is not None:
        with answers_file.open() as f:
            answers = yaml.safe_load(f)
    else:
        answers = None

    run_copy(
        str(SOURCE_DIR),
        str(project_dir),
        data=answers,
    )

def main() -> None:
    """Main function."""
    app()

if __name__ == "__main__":
    main()
