def find_paths(lab, row, col, direction, path):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return

    if lab[row][col] == '*' or lab[row][col] == 'v':
        return

    path.append(direction)

    if lab[row][col] == 'e':
        print(''.join(path))
    else:
        lab[row][col] = 'v'
        find_paths(lab, row, col + 1, 'R', path)
        find_paths(lab, row, col - 1, 'L', path)
        find_paths(lab, row + 1, col, 'D', path)
        find_paths(lab, row - 1, col, 'U', path)
        lab[row][col] = '-'

    path.pop()


rows = int(input())
cols = int(input())
lab = []

for _ in range(rows):
    lab.append(list(input()))

find_paths(lab, 0, 0, '', [])