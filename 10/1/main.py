import re
from itertools import combinations
from functools import cache

@cache
def apply_press(state: tuple[int, ...], press: tuple[int, ...]) -> tuple[int, ...]:
    new_state = list(state)
    for pos in press:
        new_state[pos] ^= 1
    return tuple(new_state)

def solve_row(pattern: tuple[int, ...], buttons: list[tuple[int, ...]]) -> int:
    for n in range(len(buttons)):
        for press_sequence in combinations(buttons, r=n + 1):
            state = tuple([0] * len(pattern))
            for i, press in enumerate(press_sequence):
                state = apply_press(state, press)
                if state == pattern:
                    return i + 1
    raise RuntimeError("No solution found")

def solve(input_lines: list[str]):
    top_re = re.compile(r"^\[(?P<pattern>[.#]*)\](?P<buttons>(\s\([\d,]*\))*)\s\{(?P<joltage>[\d,]*)\}$")
    button_re = re.compile(r"\(([\d,]*)\)")

    total = 0
    for line in input_lines:
        if not (match := top_re.match(line)):
            raise ValueError(f"Invalid line: {line}")
        pattern = tuple([1 if c == "#" else 0 for c in match.group("pattern")])
        buttons = list(map(lambda s: tuple(map(int, s.split(","))), button_re.findall(match.group("buttons"))))
        joltage = list(map(int, match.group("joltage").split(",")))
        total += solve_row(pattern, buttons)

    return total


def main():
    with open("10/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
