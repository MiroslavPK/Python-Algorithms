def dfs(matrix, row, col, visited, parent):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[row]):
        return
    if visited[row][col]:
        return
    if matrix[row][col] != parent:
        return
    visited[row][col] = True
    dfs(matrix, row + 1, col, visited, parent)
    dfs(matrix, row - 1, col, visited, parent)
    dfs(matrix, row, col + 1, visited, parent)
    dfs(matrix, row, col - 1, visited, parent)


rows = int(input())
cols = int(input())
matrix = []
visited = []
connected_areas = {}

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)


for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        parent = matrix[row][col]
        if parent not in connected_areas:
            connected_areas[parent] = 1
        else:
            connected_areas[parent] += 1
        dfs(matrix, row, col, visited, parent)

num_of_areas = sum(connected_areas.values())
# connected_areas = dict(sorted(connected_areas.items(), key=lambda k: k[0]))
print(f'Areas: {num_of_areas}')
for k, v in sorted(connected_areas.items()):
    print(f"Letter '{k}' -> {v}")
