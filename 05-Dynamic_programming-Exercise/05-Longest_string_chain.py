from collections import deque

words = input().split()

size = [0] * len(words)
prev = [-1] * len(words)

best_size = 0
best_idx = 0

for current_idx in range(len(words)):
    current_word = words[current_idx]
    current_size = 1
    parent = -1
    for previous_idx in range(current_idx - 1, -1, -1):
        previous_word = words[previous_idx]

        if len(previous_word) >= len(current_word):
            continue

        if size[previous_idx] + 1 >= current_size:
            current_size = size[previous_idx] + 1
            parent = previous_idx

    size[current_idx] = current_size
    prev[current_idx] = parent

    if current_size > best_size:
        best_size = current_size
        best_idx = current_idx


lis = deque()
idx = best_idx
while idx != -1:
    lis.appendleft(words[idx])
    idx = prev[idx]

print(*lis)
