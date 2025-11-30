import shutil
import typer
import httpx
from datetime import datetime
import os


app = typer.Typer()


main_template = """
def solve(input_lines: list[str]):
    pass


def main():
    with open("{0}/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
""".lstrip()

test_template = """
from main import solve


def test_main():
    assert solve([

    ]) == 0
""".lstrip()


@app.command()
def new_day(
    day: int = typer.Option(datetime.now().day),
    session_cookie: str = typer.Option(None),
    email: str = typer.Option(None),
    year: int = typer.Option(datetime.now().year)
):
    padded = str(day).zfill(2)
    print(f"Creating day {padded}")

    if os.path.isdir(padded):
        raise Exception(f"Folder {padded} already exists")

    os.mkdir(padded)
    os.mkdir(f"{padded}/1")
    os.mkdir(f"{padded}/2")

    with open(f"{padded}/1/main.py", "w") as f:
        f.writelines(main_template.format(padded))
    
    with open(f"{padded}/1/test_main_{padded}_1.py", "w") as f:
        f.writelines(test_template)

    if not session_cookie:
        print("No session cookie specified. Skipping download")
        return

    url = f"https://adventofcode.com/{year}/day/{day}/input"

    print(f"Downloading: {url}")

    r = httpx.get(
        url,
        headers={
            "Cookie": f"session={session_cookie}",
            "User-Agent": f"https://github.com/tituszban/advent_of_code_2024 by {email}"
        },
        verify=False)

    with open(f"{padded}/input.txt", "w") as f:
        f.writelines(r.text)


@app.command()
def part_two(day: int = typer.Option(datetime.now().day)):
    padded = str(day).zfill(2)
    print(f"Creating part 2 of day {padded}")

    if not os.path.isdir(padded):
        raise Exception(f"Folder {padded} doesn't exist")

    if os.path.isfile(f"{padded}/2/main.py"):
        raise Exception(f"Part 2 file of {padded} already exists")

    shutil.copy2(f"{padded}/1/main.py", f"{padded}/2/main.py")

    if os.path.isfile(f"{padded}/2/test_main_{padded}_2.py"):
        raise Exception(f"Tests for {padded} already exists")
    
    if os.path.isfile(f"{padded}/1/test_main_{padded}_1.py"):
        shutil.copy2(f"{padded}/1/test_main_{padded}_1.py", f"{padded}/2/test_main_{padded}_2.py")


if __name__ == "__main__":
    app()
