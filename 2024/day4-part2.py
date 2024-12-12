def read_grid(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def count_xmas_in_grid(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    def is_in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def is_valid_xmas(x, y):
        if not (is_in_bounds(x-1, y-1) and is_in_bounds(x+1, y+1)):
            return False
        if not (is_in_bounds(x-1, y+1) and is_in_bounds(x+1, y-1)):
            return False

        ul_dr = (
            (grid[x-1][y-1] == 'M' and grid[x][y] == 'A' and grid[x+1][y+1] == 'S') or
            (grid[x-1][y-1] == 'S' and grid[x][y] == 'A' and grid[x+1][y+1] == 'M')
        )
        ur_dl = (
            (grid[x-1][y+1] == 'M' and grid[x][y] == 'A' and grid[x+1][y-1] == 'S') or
            (grid[x-1][y+1] == 'S' and grid[x][y] == 'A' and grid[x+1][y-1] == 'M')
        )
        return ul_dr and ur_dl

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 'A' and is_valid_xmas(x, y):
                count += 1

    return count

if __name__ == "__main__":
    grid = read_grid("input4.txt")
    total_count = count_xmas_in_grid(grid)
    print(f"Total X-MAS occurrences: {total_count}")