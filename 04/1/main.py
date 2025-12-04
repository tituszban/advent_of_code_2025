import numpy as np
from scipy.signal import convolve2d

def solve(input_lines: list[str]):
    grid = np.array([
        list(map(lambda c: 1 if c == "@" else 0, line)) for line in input_lines
    ])
    kernel = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ])

    conv = convolve2d(grid, kernel, mode="same", boundary="fill", fillvalue=0)

    total = ((conv < 4) * grid).sum()

    return total


def main():
    with open("04/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
