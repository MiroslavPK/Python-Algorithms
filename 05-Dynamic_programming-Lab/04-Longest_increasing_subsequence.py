from collections import deque

nums = [int(x) for x in input().split()]

size = [1] * len(nums)
parent = [-1] * len(nums)

best_len = 1
best_idx = 0

for current in range(1, len(nums)):
    curr_num = nums[current]
    curr_len = 1
    curr_parent = -1
    for previous in range(current - 1, -1, -1):
        prev_num = nums[previous]
        if prev_num >= curr_num:
            continue

        if size[previous] + 1 >= curr_len:
            curr_len = size[previous] + 1
            curr_parent = previous

        size[current] = curr_len
        parent[current] = curr_parent
        if curr_len > best_len:
            best_len = curr_len
            best_idx = current

lis = deque()
idx = best_idx
while idx != -1:
    lis.appendleft(nums[idx])
    idx = parent[idx]

print(*lis)
