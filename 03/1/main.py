from collections import defaultdict

def solve(input_lines: list[str]):
    t = 0
    for line in input_lines:
        nums = defaultdict(list)
        for n, c in enumerate(line):
            nums[int(c)].append(n)

        print(line)
        print(nums)

        c = 0
        first_index = 0
        last = len(line) - 1
        for n in range(9, -1, -1):
            if n not in nums:
                continue
            first_index = nums[n].pop(0)
            if first_index == last:
                nums[n].insert(0, first_index)
                continue
            c = n * 10
            break

        print(c)
        
        for n in range(9, -1, -1):
            if n not in nums or not nums[n]:
                continue

            ind = nums[n].pop()
            if first_index > ind:
                continue
            c += n
            break
        print(c)

        t += c

    return t



def main():
    with open("03/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
