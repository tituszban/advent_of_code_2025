def solve(input_lines: list[str]):
    beam = [0 for _ in range(len(input_lines[0]))]

    for line in input_lines:
        new_beam = [0 for _ in range(len(input_lines[0]))]
        for i, c in enumerate(line):
            if c == 'S':
                new_beam[i] = 1
            elif c == '^' and beam[i] > 0:
                new_beam[i - 1] += beam[i]
                new_beam[i + 1] += beam[i]
            else:
                new_beam[i] += beam[i]
        beam = new_beam

    return sum(beam)


def main():
    with open("07/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
