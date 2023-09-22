def calc_factorial(num):
    if num <= 1:
        return 1
    return num * calc_factorial(num - 1)


n = int(input() or 5)

print(calc_factorial(n))