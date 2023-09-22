def insertion_sort(nums):
    i = 1
    while i < len(nums):
        j = i
        while j >= 1 and nums[j] < nums[j - 1]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
        i = i + 1
    return nums


nums = [int(x) for x in input().split()]
sorted_arr = insertion_sort(nums)
print(*sorted_arr)
