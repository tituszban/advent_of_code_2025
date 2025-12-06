from functools import reduce
from operator import mul

def solve(input_lines: list[str]):
    z = list(zip(*[line.split() for line in input_lines]))
    total = 0

    for *v, op in z:
        if op == "+":
            total += sum(map(int, v))
        elif op == "*":
            total += reduce(mul, map(int, v))

    return total


def main():
    with open("06/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
