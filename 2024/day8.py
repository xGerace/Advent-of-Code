def solve_day8(input_file):
    grid = []
    with open(input_file, 'r') as f:
        for line in f:
            grid.append(line.rstrip('\n'))

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    positions = {}
    for r in range(rows):
        row_len = len(grid[r])
        for c in range(row_len):
            char = grid[r][c]
            if char != '.':
                positions.setdefault(char, []).append((r, c))

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    antinodes = set()

    for freq, coords in positions.items():
        if len(coords) < 2:
            continue

        for i in range(len(coords)):
            x1, y1 = coords[i]
            for j in range(i + 1, len(coords)):
                x2, y2 = coords[j]

                p1x = 2 * x1 - x2
                p1y = 2 * y1 - y2
                if in_bounds(p1x, p1y):
                    antinodes.add((p1x, p1y))

                p2x = 2 * x2 - x1
                p2y = 2 * y2 - y1
                if in_bounds(p2x, p2y):
                    antinodes.add((p2x, p2y))

    return len(antinodes)

if __name__ == "__main__":
    answer = solve_day8("input8.txt")
    print("Number of unique antinodes within the map:", answer)