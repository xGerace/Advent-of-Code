def read_grid(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def count_word_in_grid(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),  # Horizontal right
        (1, 0),  # Vertical down
        (1, 1),  # Diagonal down-right
        (1, -1), # Diagonal down-left
        (0, -1), # Horizontal left
        (-1, 0), # Vertical up
        (-1, -1),# Diagonal up-left
        (-1, 1)  # Diagonal up-right
    ]

    def is_in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def find_word(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_in_bounds(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if find_word(x, y, dx, dy):
                    count += 1
    return count

if __name__ == "__main__":
    grid = read_grid("input4.txt")
    word = "XMAS"
    total_count = count_word_in_grid(grid, word)
    print(f"Total occurrences of {word}: {total_count}")