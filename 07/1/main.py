def solve(input_lines: list[str]):
    beam = [0 for _ in range(len(input_lines[0]))]

    split = 0
    for line in input_lines:
        for i, c in enumerate(line):
            if c == 'S':
                beam[i] = 1
            elif c == '^' and beam[i] == 1:
                beam[i - 1] = 1
                beam[i] = 0
                beam[i + 1] = 1
                split += 1

    return split


def main():
    with open("07/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
