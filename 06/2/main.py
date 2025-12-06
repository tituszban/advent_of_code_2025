from functools import reduce
from operator import mul, add

def solve(input_lines: list[str]):
    z = list(reversed(list(zip(*input_lines))))

    total = 0
    nums = []

    for *d, op in z:
        if all(di == ' ' for di in d):
            continue
        nums.append(int(''.join(d).strip()))
        if op == '+':
            total += reduce(add, nums, 0)
            nums.clear()
        elif op == '*':
            total += reduce(mul, nums, 1)
            nums.clear()

    return total



def main():
    with open("06/input.txt") as f:
        test_input = list(map(lambda line: line.rstrip("\n"), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
