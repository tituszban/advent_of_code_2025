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
    total = 0

    while True:
        conv = convolve2d(grid, kernel, mode="same", boundary="fill", fillvalue=0)

        to_remove = (conv < 4) & (grid == 1)
        if not to_remove.any():
            return total

        total += (to_remove).sum()
        grid[to_remove] = 0



def main():
    with open("04/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
