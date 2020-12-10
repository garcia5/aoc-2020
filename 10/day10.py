def read_input_sorted(file='input'):
    return sorted([int(l.strip()) for l in open(file, 'r')])


def walk_chain(adapters):

    # initial 0 and device max + 3
    adapters.insert(0, 0)
    adapters.append(max(adapters) + 3)

    counts = {k: 0 for k in range(1, 4)}

    for i in range(len(adapters) - 1):
        diff = adapters[i + 1] - adapters[i]
        counts[diff] += 1

    print(counts)


# print(read_input_sorted())
walk_chain(read_input_sorted())
