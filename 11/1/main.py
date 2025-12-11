def solve(input_lines: list[str]):
    graph = {
        sp[0]: sp[1].split(" ")
        for line in input_lines
        if (sp := line.split(": "))
    }

    def find_all_paths(current: str, target: str) -> int:
        if current == target:
            return 1
        
        if current not in graph:
            return 0
        
        path_count = 0
        
        for neighbor in graph[current]:
            path_count += find_all_paths(neighbor, target)
        
        return path_count
    
    return find_all_paths("you", "out")


def main():
    with open("11/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
