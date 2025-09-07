from pathlib import Path
from typing import Annotated

import typer
import yaml
from copier import run_copy

if __package__ is None:
    ROOT_DIR = Path(__file__).parent.parent
    SOURCE_DIR = ROOT_DIR / "project"
    if not SOURCE_DIR.exists():
        raise FileNotFoundError(
            "Run as a script, but project directory is not complete,",
            f"  missing: {SOURCE_DIR}.",
        )
else:
    SOURCE_DIR = Path(str(__package__)) / "template"
    if not SOURCE_DIR.exists():
        raise FileNotFoundError(
            f"Unexpected Error: template directory not found: {SOURCE_DIR}.",
            "Please report this issue to the project maintainer.",
        )

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

    print(SOURCE_DIR)
    print(project_dir)
    print(answers)
    return

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
