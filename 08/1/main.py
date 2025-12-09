from operator import mul
from functools import reduce

def dist(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2

def solve(input_lines: list[str], n: int = 1000):
    nums = [tuple(map(int, line.split(","))) for line in input_lines]

    dists = {}

    for i, p1 in enumerate(nums):
        for p2 in nums[i + 1:]:
            d = dist(p1, p2)
            dists[(p1, p2)] = d
    dists_sorted = sorted(dists.items(), key=lambda x: x[1])[:n]

    circuits: list[set[tuple[int, int, int]]] = []

    for (p1, p2), _ in dists_sorted:
        found_in_circuits = [c for c in circuits if p1 in c or p2 in c]
        if len(found_in_circuits) == 0:
            circuits.append(set([p1, p2]))
        elif len(found_in_circuits) == 1:
            found_in_circuits[0].add(p1)
            found_in_circuits[0].add(p2)
        else:
            new_circuit = set()
            for c in found_in_circuits:
                new_circuit.update(c)
                circuits.remove(c)
            new_circuit.add(p1)
            new_circuit.add(p2)
            circuits.append(new_circuit)
    
    top_circuits = sorted(circuits, key=lambda x: len(x), reverse=True)[:3]

    return reduce(mul, (len(c) for c in top_circuits), 1)



def main():
    with open("08/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
