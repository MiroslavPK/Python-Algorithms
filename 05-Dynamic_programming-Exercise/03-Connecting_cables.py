cables = [int(x) for x in input().split()]

lcs = []
size = len(cables) + 1

connections = [num for num in range(1, size)]
[lcs.append([0] * size) for _ in range(size)]


for row in range(1, size):
    for col in range(1, size):
        if cables[row - 1] == connections[col - 1]:
            lcs[row][col] = lcs[row - 1][col - 1] + 1
        else:
            up = lcs[row-1][col]
            left = lcs[row][col-1]
            lcs[row][col] = max(up, left)

print(f'Maximum pairs connected: {lcs[size - 1][size - 1]}')
