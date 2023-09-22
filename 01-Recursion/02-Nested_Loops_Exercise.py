def nested_loops(n, arr):
    if len(arr) == n:
        print(*arr)
        return

    for i in range(1, n + 1):
        arr.append(i)
        nested_loops(n, arr)
        arr.pop()


n = int(input())
nested_loops(n, [])
