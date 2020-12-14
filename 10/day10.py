def read_input_sorted(file="input"):
    return sorted([int(l.strip()) for l in open(file, "r")])


def valid_chain(adapters: list[int]) -> bool:

    # initial 0 and device max + 3
    adapters.insert(0, 0)
    adapters.append(max(adapters) + 3)

    for i in range(len(adapters) - 1):
        diff = adapters[i + 1] - adapters[i]
        if diff > 3:
            return False

    return True


SEEN_COUNTS = {}


def get_chains(remaining: list[int], min_a: int):
    start_idx = remaining.index(min_a) + 1
    remaining_copy = remaining[start_idx:]

    if len(remaining_copy) == 1:
        return 1

    # get all possible next chain values
    next_adapters = [a for a in remaining_copy if a <= min_a + 3]

    count = 0
    for a in next_adapters:
        # assume we start with a, how many permutations are left?
        if SEEN_COUNTS.get(a):
            count += SEEN_COUNTS[a]
        else:
            this_count = get_chains(remaining_copy, a)
            SEEN_COUNTS[a] = this_count
            count += this_count

    return count


# find all subsets of adapter where the chain can be walked
init_list = read_input_sorted()
init_list.insert(0, 0)
init_list.append(max(init_list) + 3)

# generate all subsets (sub lists)
print(get_chains(init_list, 0))
