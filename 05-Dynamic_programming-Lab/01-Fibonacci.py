def fibonacci(n, memory):
    if n in memory:
        return memory[n]
    if n <= 2:
        return 1
    res = fibonacci(n-1, memory) + fibonacci(n-2, memory)
    memory[n] = res
    return res


n = int(input())
mem = {}

result = fibonacci(n, mem)
print(result)
