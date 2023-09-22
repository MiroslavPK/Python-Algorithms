def move_out(grid, row, col, direction, path, paths):
    if row >= len(grid) or col >= len(grid[0]):
        return
    
    path += direction
    if grid[row][col] == 'e' and path not in paths:
        paths.append(path)

    move_out(grid, row, col + 1, 'R', path, paths)
    move_out(grid, row + 1, col, 'D', path, paths)
    return len(paths)


rows = int(input())
cols = int(input())
grid = []
for i in range(rows):
    grid.append(['-'] * cols)
grid[rows - 1][cols - 1] = 'e'

print(move_out(grid, 0, 0, '', '', []))
