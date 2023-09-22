def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


nums = [int(x) for x in input().split()]
sorted_arr = bubble_sort(nums)
print(*sorted_arr)