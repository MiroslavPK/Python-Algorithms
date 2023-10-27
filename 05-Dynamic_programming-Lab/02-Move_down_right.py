rows = int(input())
cols = int(input())
matrix = []
dp = [[0] * cols for _ in range(rows)]

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

dp[0][0] = matrix[0][0]

for col in range(1, cols):
    dp[0][col] = dp[0][col - 1] + matrix[0][col]

for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + matrix[row][0]

for row in range(1, rows):
    for col in range(1, cols):
        dp[row][col] = max(dp[row-1][col], dp[row][col-1]) + matrix[row][col]

row = rows - 1
col = cols - 1

reversed_path = []
while row > 0 and col > 0:
    reversed_path.append([row, col])
    if dp[row][col-1] >= dp[row-1][col]:
        col -= 1
    else:
        row -= 1

while row > 0:
    reversed_path.append([row, col])
    row -= 1

while col > 0:
    reversed_path.append([row, col])
    col -= 1

reversed_path.append([0, 0])
for couple in reversed_path[-1::-1]:
    print(f'{couple}', end=' ')
