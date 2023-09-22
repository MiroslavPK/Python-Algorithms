def calc_fibonacci(n):
    global fib_mem
    if n in fib_mem:
        return fib_mem[n]
    if n <= 1:
        return 1
    memorize = calc_fibonacci(n - 1) + calc_fibonacci(n - 2)
    fib_mem[n] = memorize
    return memorize


fib_mem = dict()
n = int(input() or 5)
print(calc_fibonacci(n))