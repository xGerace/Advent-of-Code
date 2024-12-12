def solve_guard_path(grid):
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }
    direction_order = ['^', '>', 'v', '<'] 

    start_pos = None
    start_dir = None
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val in directions:
                start_pos = (r, c)
                start_dir = val
                break
        if start_pos is not None:
            break

    visited = set([start_pos])
    rows = len(grid)
    cols = len(grid[0])

    current_pos = start_pos
    current_dir = start_dir

    def next_in_front(pos, d):
        dr, dc = directions[d]
        return pos[0] + dr, pos[1] + dc

    while True:
        nr, nc = next_in_front(current_pos, current_dir)

        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
            break

        if grid[nr][nc] == '#':
            dir_idx = direction_order.index(current_dir)
            current_dir = direction_order[(dir_idx + 1) % 4]
            continue
        else:
            current_pos = (nr, nc)
            visited.add(current_pos)

    return len(visited)

if __name__ == "__main__":
    with open("input6.txt", "r") as f:
        input_lines = [line.rstrip("\n") for line in f]

    grid = [list(line) for line in input_lines]
    result = solve_guard_path(grid)
    print("Number of distinct visited positions:", result)