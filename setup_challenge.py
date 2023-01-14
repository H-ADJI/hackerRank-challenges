import typer
import os
import time
import re
from pathlib import Path
CHALLENGES_PATH = "./challenges"
FILES_NAME_PATTERN = r".+(?=\.py)"
cli = typer.Typer()


@cli.command()
def all_solved():
    challenge_files = os.listdir(CHALLENGES_PATH)
    for file_name in challenge_files:
        print(re.search(pattern=FILES_NAME_PATTERN, string=file_name).group())
        print(time.ctime(os.path.getctime(Path(CHALLENGES_PATH).joinpath(file_name))))


@cli.command()
def last_solved():
    pass


@cli.command()
def solved_count():
    pass


if __name__ == "__main__":
    cli()
