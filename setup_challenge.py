import typer
import os
import time
from utils.utils import get_challenge_name, get_file_creation_date, challenge_files, CHALLENGES_PATH
import re
from pathlib import Path
from rich import print as rprint
from rich.console import Console
from rich.table import Table

console = Console()
cli = typer.Typer()


@cli.command()
def all_solved():
    for file_name in challenge_files:
        challenges_table.add_row(get_challenge_name(
            file_name=file_name), time.ctime(get_file_creation_date(file_name=file_name)))
    console.print(challenges_table)


@cli.command()
def last_solved():
    last = [0, None]
    for file_name in challenge_files:
        creation_time = get_file_creation_date(file_name=file_name)
        if last[0] <= creation_time:
            last = [creation_time,
                    get_challenge_name(file_name=file_name)]
    rprint(last)


@cli.command()
def solved_count():
    rprint(f"You solved {len(challenge_files)} problem so far")


@cli.command()
def new_challenge(challenge_name: str, author: str = "KHALIL HADJI"):
    with open(Path(CHALLENGES_PATH).joinpath(f"{challenge_name}.py"), "w") as challenge, open("./utils/template.txt", "r") as t:
        template = t.read()
        challenge.write(template.format(
            challenge_name=challenge_name, author=author))
    rprint(f"A file for Challenge {(challenge_name)} was just created, make sure to write the function body and setup the corect input arguments")


if __name__ == "__main__":
    challenges_table = Table("challenge name", "solved on")
    cli()
