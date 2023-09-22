def draw(lgt):
    if lgt <= 0:
        return

    print("*" * lgt)
    draw(lgt - 1)
    print("#" * lgt)


length = int(input())

draw(length)
