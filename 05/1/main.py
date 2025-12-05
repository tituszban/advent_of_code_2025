from functools import reduce


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged = []
    for current in ranges:
        if not merged or merged[-1][1] < current[0] - 1:
            merged.append(current)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], current[1]))
    return merged


def solve(input_lines: list[str]):
    ranges, ingredients = reduce(
        lambda acc, line: (
            (acc[0], [])
            if line == ""
            else ([*acc[0], tuple(map(int, line.split("-")))], acc[1])
            if acc[1] is None
            else (acc[0], [*acc[1], int(line)])
        ),
        input_lines,
        ([], None))
    
    ranges = merge_ranges(sorted(ranges))
    ingredients = sorted(set(ingredients))

    count = 0
    current_range = ranges.pop(0)

    while ingredients:
        ingredient = ingredients.pop(0)
        
        while ingredient > current_range[1] and ranges:
            current_range = ranges.pop(0)

        if ingredient > current_range[1]:
            break
        if ingredient < current_range[0]:
            continue

        assert current_range[0] <= ingredient <= current_range[1], "If this fails, the logic is wrong"
        count += 1

    return count


def main():
    with open("05/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
