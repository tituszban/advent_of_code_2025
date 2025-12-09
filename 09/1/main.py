def solve(input_lines: list[str]):
    corners = [tuple(map(int, line.split(","))) for line in input_lines]

    max_area = 0
    for i, c1 in enumerate(corners):
        for c2 in corners[i + 1:]:
            x1, x2 = sorted([c1[0], c2[0]])
            y1, y2 = sorted([c1[1], c2[1]])
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            if area > max_area:
                print(x1, y1, x2, y2, area)
                max_area = area

    return max_area


def main():
    with open("09/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
