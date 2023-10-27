from collections import deque

str1 = input()
str2 = input()

rows = len(str1) + 1
cols = len(str2) + 1

lcs = []
[lcs.append([0] * cols) for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if str1[row - 1] == str2[col - 1]:
            prev = lcs[row - 1][col - 1]
            lcs[row][col] = prev + 1
        else:
            up = lcs[row-1][col]
            left = lcs[row][col-1]
            lcs[row][col] = max(up, left)

lcs_letters = deque()
row = rows - 1
col = cols - 1

while row > 0 and col > 0:
    if str1[row - 1] == str2[col - 1]:
        lcs_letters.appendleft(str1[row - 1])
        row -= 1
        col -= 1
    elif lcs[row - 1][col] > lcs[row][col - 1]:
        row -= 1
    else:
        col -= 1

print(len(lcs_letters))
