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

    visited_positions = set([start_pos])
    rows = len(grid)
    cols = len(grid[0])
    current_pos = start_pos
    current_dir = start_dir

    visited_states = set()
    visited_states.add((current_pos[0], current_pos[1], current_dir))

    def next_in_front(pos, d):
        dr, dc = directions[d]
        return pos[0] + dr, pos[1] + dc

    while True:
        nr, nc = next_in_front(current_pos, current_dir)

        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
            return (len(visited_positions), True, visited_states)

        if grid[nr][nc] == '#':
            dir_idx = direction_order.index(current_dir)
            current_dir = direction_order[(dir_idx + 1) % 4]
        else:
            current_pos = (nr, nc)
            visited_positions.add(current_pos)

        state = (current_pos[0], current_pos[1], current_dir)
        if state in visited_states:
            return (len(visited_positions), False, visited_states)
        visited_states.add(state)

def find_loop_positions(grid):
    directions = {'^', 'v', '<', '>'}
    start_pos = None
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val in directions:
                start_pos = (r, c)
                break
        if start_pos is not None:
            break

    rows = len(grid)
    cols = len(grid[0])

    loop_positions = 0

    for r in range(rows):
        for c in range(cols):
            if (r, c) != start_pos and grid[r][c] == '.':
                original_char = grid[r][c]
                grid[r][c] = '#'
                
                visited_count, left_grid, _ = solve_guard_path(grid)
                
                if not left_grid:
                    loop_positions += 1
                
                grid[r][c] = original_char

    return loop_positions

if __name__ == "__main__":
    with open("input6.txt", "r") as f:
        input_lines = [line.rstrip("\n") for line in f]

    grid = [list(line) for line in input_lines]

    result = find_loop_positions(grid)
    print("Number of possible loop-creating positions:", result)