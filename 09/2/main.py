from collections import defaultdict

def solve(input_lines: list[str], scale: int = 800, n: int = 300) -> int:
    # Both the example and the input are clockwise
    corners = [tuple(map(int, line.split(","))) for line in input_lines]

    xs = sorted({x for x, _ in corners})
    ys = sorted({y for _, y in corners})

    x_borders = defaultdict(set)
    y_borders = defaultdict(set)


    drag_grid = {(x, y): " " for x in range(min(xs) // scale, max(xs) // scale + 1) for y in range(min(ys) // scale, max(ys) // scale + 1)}

    for i, (p1, p2) in enumerate(zip(corners, corners[1:] + [corners[0]])):
        x1, y1 = p1
        x2, y2 = p2

        if x1 == x2:
            x_borders[x1].add((min(y1, y2), max(y1, y2)))
        else:
            y_borders[y1].add((min(x1, x2), max(x1, x2)))

        char = ["a", "b", "c", "d"][i % 4]

        if x1 == x2:
            for y in range(min(y1, y2) // scale, max(y1, y2) // scale + 1):
                drag_grid[(x1 // scale, y)] = char
        else:
            for x in range(min(x1, x2) // scale, max(x1, x2) // scale + 1):
                drag_grid[(x, y1 // scale)] = char

    cells = {(x1, x2, y1, y2): 0 for x1, x2 in zip(xs[:-1], xs[1:]) for y1, y2 in zip(ys[:-1], ys[1:])}

    
    # flood fill
    start_x = corners[n][0], xs[xs.index(corners[n][0]) + 1]
    start_y = corners[n][1], ys[ys.index(corners[n][1]) + 1]

    to_visit = [(start_x[0], start_x[1], start_y[0], start_y[1])]
    while to_visit:
        cell = to_visit.pop()
        if cells[cell] == 1:
            continue

        cells[cell] = 1

        x1, x2, y1, y2 = cell

        for x in range(x1 // scale, x2 // scale + 1):
            for y in range(y1 // scale, y2 // scale + 1):
                drag_grid[(x, y)] = "."

        # check neighbors
        # left
        if x1 in x_borders:
            if not any(y1 < by2 and y2 > by1 for by1, by2 in x_borders[x1]):
                if xs.index(x1) - 1 >= 0:
                    neighbor = (xs[xs.index(x1) - 1], x1, y1, y2)
                    if cells[neighbor] == 0:
                        to_visit.append(neighbor)

        # right
        if x2 in x_borders:
            if not any(y1 < by2 and y2 > by1 for by1, by2 in x_borders[x2]):
                if xs.index(x2) + 1 < len(xs):
                    neighbor = (x2, xs[xs.index(x2) + 1], y1, y2)
                    if cells[neighbor] == 0:
                        to_visit.append(neighbor)

        # down
        if y1 in y_borders:
            if not any(x1 < bx2 and x2 > bx1 for bx1, bx2 in y_borders[y1]):
                if ys.index(y1) - 1 >= 0:
                    neighbor = (x1, x2, ys[ys.index(y1) - 1], y1)
                    if cells[neighbor] == 0:
                        to_visit.append(neighbor)

        # up
        if y2 in y_borders:
            if not any(x1 < bx2 and x2 > bx1 for bx1, bx2 in y_borders[y2]):
                if ys.index(y2) + 1 < len(ys):
                    neighbor = (x1, x2, y2, ys[ys.index(y2) + 1])
                    if cells[neighbor] == 0:
                        to_visit.append(neighbor)

    
    for y in range(min(ys) // scale, max(ys) // scale + 1):
        row = ""
        for x in range(min(xs) // scale, max(xs) // scale + 1):
            row += str(drag_grid[(x, y)])
        print(row)

    max_area = 0
    for i, c1 in enumerate(corners):
        for c2 in corners[i + 1:]:
            x1, x2 = sorted([c1[0], c2[0]])
            y1, y2 = sorted([c1[1], c2[1]])

            empty_cell = False
            for x in range(xs.index(x1), xs.index(x2)):
                for y in range(ys.index(y1), ys.index(y2)):
                    cell = (xs[x], xs[x + 1], ys[y], ys[y + 1])
                    if cells[cell] == 0:
                        empty_cell = True
                        break
                else:
                    continue
                break
            if empty_cell:
                continue

            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            if area > max_area:
                max_area = area

    return max_area

def main():
    with open("09/input.txt") as f:
        test_input = list(map(lambda line: line.strip(), f.readlines()))

    print(solve(test_input))


if __name__ == "__main__":
    main()
