def gen01(vector, idx):
    if idx >= len(vector):
        # print(''.join([str(n) for n in vector]))
        print(*vector, sep='')
        return

    for n in range(2):
        vector[idx] = n
        gen01(vector, idx + 1)


n = int(input())
vector = [0] * n
gen01(vector, 0)
