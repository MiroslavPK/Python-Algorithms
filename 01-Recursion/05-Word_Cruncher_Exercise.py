def word_crunch(idx, word_container, word_count, used_slices, target):
    if idx >= len(target):
        print(' '.join(used_slices))
        return
    if idx not in word_container:
        return

    for word in word_container[idx]:
        if word_count[word] == 0:
            continue
        used_slices.append(word)
        word_count[word] -= 1

        word_crunch(idx + len(word), word_container, word_count, used_slices, target)

        word_count[word] += 1
        used_slices.pop()


words = input().split(', ')
target = input()
word_container = {}
word_count = {}

for word_slice in words:
    if word_slice in word_count:
        word_count[word_slice] += 1
        continue
    word_count[word_slice] = 1

    try:
        idx = 0
        while True:
            idx = target.index(word_slice, idx)
            if idx not in word_container:
                word_container[idx] = []
            word_container[idx].append(word_slice)
            idx += len(word_slice)
    except ValueError:
        pass

word_crunch(0, word_container, word_count, [], target)
