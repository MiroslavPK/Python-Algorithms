class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def find_areas(matrix, row, col):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0

    if matrix[row][col] != '-':
        return 0

    matrix[row][col] = 'v'
    
    result = 1
    result += find_areas(matrix, row + 1, col)
    result += find_areas(matrix, row - 1, col)
    result += find_areas(matrix, row, col + 1)
    result += find_areas(matrix, row, col - 1)
    
    return result


rows = int(input())
cols = int(input())
matrix = [list(input()) for row in range(rows)]

areas = []
for row in range(rows):
    for col in range(cols):
        size = find_areas(matrix, row, col)
        if size != 0:
            areas.append(Area(row, col, size))

print(f'Total areas found: {len(areas)}')
for i, area in enumerate(sorted(areas, key=lambda a: a.size, reverse=True)):
    print(f'Area #{i+1} at ({area.row}, {area.col}), size: {area.size}')