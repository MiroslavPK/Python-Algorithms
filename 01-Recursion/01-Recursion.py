def recursive_sum(numbers, idx):
    if idx == len(numbers) - 1:
        return numbers[idx]
    return numbers[idx] + recursive_sum(numbers, idx + 1)


nums = [int(num) for num in input().split() or [3, 4, 5, 6]]

print(recursive_sum(nums, 0))