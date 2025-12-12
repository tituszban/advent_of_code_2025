import re

def solve(input_lines: list[str]):
    shapes = []
    current_shape = []
    areas = []
    for line in input_lines:
        if re.match(r"^\d:$", line):
            continue
        if (m := re.match(r"^[#.]+$", line)):
            current_shape.append([c == "#" for c in line])
            continue
        if line == "":
            shapes.append(current_shape)
            current_shape = []
            continue
        if (m := re.match(r"^(\d+)x(\d+): ([\d\s]+)$", line)):
            width, height, boxes = m.groups()
            areas.append((int(width), int(height), list(map(int, boxes.split()))))
            continue
        assert False, f"Unmatched line: {line}"


    count = 0
    for w, h, boxes in areas:
        total_area = w * h
        box_area = sum([sum(line) * count for box, count in enumerate(boxes) for line in shapes[box]])
        # I hate that this works.
        if box_area > total_area:
            print(total_area, box_area, total_area - box_area)
        else:
            count += 1

    return count


def main():
    with open("12/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
