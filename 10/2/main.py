import re
from scipy.optimize import linprog

def solve_row(counts: tuple[int, ...], buttons: list[tuple[int, ...]]) -> int:
    return linprog(
        [1 for _ in buttons],
        A_eq=[[i in button for button in buttons] for i in range(len(counts))],
        b_eq=list(counts),
        integrality=1
    ).fun
    

def solve(input_lines: list[str]):
    top_re = re.compile(r"^\[(?P<pattern>[.#]*)\](?P<buttons>(\s\([\d,]*\))*)\s\{(?P<joltage>[\d,]*)\}$")
    button_re = re.compile(r"\(([\d,]*)\)")

    total = 0
    for line in input_lines:
        if not (match := top_re.match(line)):
            raise ValueError(f"Invalid line: {line}")
        pattern = tuple([1 if c == "#" else 0 for c in match.group("pattern")])
        buttons = list(map(lambda s: tuple(map(int, s.split(","))), button_re.findall(match.group("buttons"))))
        joltage = tuple(map(int, match.group("joltage").split(",")))
        total += int(solve_row(joltage, buttons))

    return total


def main():
    with open("10/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
