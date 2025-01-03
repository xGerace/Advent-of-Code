import math

def solve_day8_part2(input_file):
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

    antinodes = set()

    for freq, coords in positions.items():
        if len(coords) < 2:
            continue

        for i in range(len(coords)):
            x1, y1 = coords[i]
            for j in range(i + 1, len(coords)):
                x2, y2 = coords[j]

                dx = x2 - x1
                dy = y2 - y1
                if dx == 0 and dy == 0:
                    continue

                g = math.gcd(dx, dy)
                step_x = dx // g
                step_y = dy // g

                cur_x, cur_y = x1, y1
                while 0 <= cur_x < rows and 0 <= cur_y < cols:
                    antinodes.add((cur_x, cur_y))
                    cur_x += step_x
                    cur_y += step_y

                cur_x, cur_y = x1, y1
                while 0 <= cur_x < rows and 0 <= cur_y < cols:
                    antinodes.add((cur_x, cur_y))
                    cur_x -= step_x
                    cur_y -= step_y

    return len(antinodes)

if __name__ == "__main__":
    answer = solve_day8_part2("input8.txt")
    print("Number of unique antinodes within the map:", answer)