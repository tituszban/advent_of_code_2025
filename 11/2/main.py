from functools import cache

def solve(input_lines: list[str]):
    graph = {
        sp[0]: sp[1].split(" ")
        for line in input_lines
        if (sp := line.split(": "))
    }


    @cache
    def find_all_paths(current: str, target: str) -> int:
        if current == target:
            return 1
        
        if current not in graph:
            return 0
        
        path_count = 0
        
        for neighbor in graph[current]:
            path_count += find_all_paths(neighbor, target)
        
        return path_count
        
    
    s1 = find_all_paths("svr", "fft")
    s2 = find_all_paths("fft", "dac")
    s3 = find_all_paths("dac", "out")
    s4 = find_all_paths("svr", "dac")
    s5 = find_all_paths("dac", "fft")
    s6 = find_all_paths("fft", "out")

    return s1 * s2 * s3 + s4 * s5 * s6


def main():
    with open("11/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
