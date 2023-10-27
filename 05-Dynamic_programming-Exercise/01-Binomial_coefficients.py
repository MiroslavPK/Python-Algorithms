def factorial(n, memo):
    if n == 2:
        return 2
    if n <= 1:
        return 1
    memo[n] = n * factorial(n - 1, memo)
    return memo[n]


n = int(input())
k = int(input())
memo = {}

result = factorial(n, memo) // (factorial(k, memo) * factorial(n-k, memo))
print(result)
