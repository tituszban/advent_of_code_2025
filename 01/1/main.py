def solve(input_lines: list[str]):
    n = 50
    c = 0

    for line in input_lines:
        direction = line[0]
        amount = int(line[1:])
        if direction == "L":
            n -= amount
        elif direction == "R":
            n += amount
        n %= 100
        if n == 0:
            c += 1
    return c


def main():
    with open("01/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
