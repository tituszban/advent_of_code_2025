def _to_equal_length_ranges(start: str, end: str):
    if len(start) == len(end):
        return [(start, end)]
    ranges = []
    _start = start
    for length in range(len(start), len(end) + 1):
        if length == len(end):
            ranges.append((_start, end))
        else:
            ranges.append(
                (_start, (length) * "9")
            ) 
            _start = "1" + (length) * "0"
    return ranges


def solve(input_line: str):
    ranges = input_line.split(",")
    nums = set()
    for r in ranges:
        start, end = r.split("-")

        for real_start, real_end in _to_equal_length_ranges(start, end):
            for le in range(1, len(real_start) // 2 + 1):
                if len(real_start) % le != 0:
                    continue
                start_half = int(real_start[:le])
                end_half = int(real_end[:le])
                for n in range(start_half, end_half + 1):
                    num = int(str(n) * (len(real_start) // le))
                    # print(num, int(real_start) <= num <= int(real_end))
                    if int(real_start) <= num <= int(real_end):
                        nums.add(num)
        # print(start, end, real_start, real_end, nums)
    return sum(nums)



def main():
    with open("02/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input[0]))


if __name__ == "__main__":
    main()
