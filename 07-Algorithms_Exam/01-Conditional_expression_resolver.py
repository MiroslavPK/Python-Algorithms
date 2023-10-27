
# from collections import deque

# expression = input().split(' ? ')

# bools = deque()
# [bools.appendleft(item) for item in expression if len(item) == 1]

# nums_sequence = expression[len(bools):]
# nums_str = nums_sequence[0].split(' : ')
# nums = [int(n) for n in nums_str]


# n = nums[0]
# k = nums[1]
# idx = 1

# while idx < len(bools) + 1:
#     cond = True if bools[idx - 1] == 't' else False
#     n = n if cond else k
#     if idx + 1 < len(nums):
#         k = nums[idx + 1]
#     idx += 1

# print(n)
