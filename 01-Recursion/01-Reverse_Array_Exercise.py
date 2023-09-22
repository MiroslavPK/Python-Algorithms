def reverse_array(arr, rev_arr, idx):
    rev_arr.append(arr[idx])
    if idx <= 0:
        return print(*rev_arr, sep=' ')

    return reverse_array(arr, rev_arr, idx - 1)


arr = list(input().split())
reverse_array(arr, [], len(arr) - 1)