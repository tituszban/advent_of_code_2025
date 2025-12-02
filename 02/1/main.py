def solve(input_line: str):
    ranges = input_line.split(",")
    total = 0
    for r in ranges:
        start, end = r.split("-")

        real_start = start if len(start) % 2 == 0 else "1" + len(start) * "0"
        real_end = end if len(end) % 2 == 0 else (len(end) - 1) * "9"

        if int(real_end) < int(real_start):
            continue

        start_half = int(real_start[: len(real_start) // 2])
        end_half = int(real_end[: len(real_end) // 2])

        for n in range(start_half, end_half + 1):
            num = int(str(n) * 2)
            # print(num, int(real_start) <= num <= int(real_end))
            if int(real_start) <= num <= int(real_end):
                total += num

        # print(start, end, "-", real_start, real_end, "-", start_half, end_half, "-", total)
    return total


def main():
    with open("02/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input[0]))


if __name__ == "__main__":
    main()
