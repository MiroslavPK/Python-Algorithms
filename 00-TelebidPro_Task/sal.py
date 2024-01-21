goats, goes = [int(x) for x in input().split()]
weights = sorted(list(map(int, input().split())), reverse=True)

raft_capacity = max(weights)
success = False

while not success:
    taken = [0] * goats

    for go in range(goes):
        left_capacity = raft_capacity
        for idx, wgt in enumerate(weights):
            if taken[idx] == 1 or wgt > left_capacity:
                continue

            left_capacity -= wgt
            taken[idx] = 1

    if all(taken):
        success = True
        print(raft_capacity)
    raft_capacity += min(weights)
