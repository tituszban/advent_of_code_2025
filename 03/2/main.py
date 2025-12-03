from collections import defaultdict

def solve(input_lines: list[str], digit_count: int = 12) -> int:
    t = 0
    for line in input_lines:
        nums = defaultdict(list)
        for n, c in enumerate(line):
            nums[int(c)].append(n)
        
        print(line)
        print(nums)
        c = 0
        last_index = 0

        for i in range(digit_count, 0, -1):
            blocked = len(line) - i
            for n in range(9, -1, -1):
                if n not in nums or not nums[n]:
                    continue
                while nums[n] and (ind := nums[n].pop(0)) < last_index:
                    continue
                if ind < last_index:
                    continue
                if ind > blocked:
                    nums[n].insert(0, ind)
                    continue
                c += n * 10 ** (i - 1)
                last_index = ind
                break

            print(i, c, blocked)

        t += c

    return t



def main():
    with open("03/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
