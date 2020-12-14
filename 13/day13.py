def get_slope(baseline, bus_id, offset):
    v1 = v2 = 0

    val = baseline
    while True:
        if val % baseline == 0 and ((val + offset) % bus_id == 0):
            if v1 == 0:
                v1 = val

            elif v2 == 0:
                v2 = val
                break

        val += baseline

    return v2 - v1


def gcd(a, b):
    if a == 0:
        return b

    if b == 0:
        return a

    return gcd(b, a - (b * int(a / b)))


if __name__ == "__main__":
    lines = [line.strip() for line in open("input2", "r")]
    earliest = int(lines[0])
    in_service = [int(_id) if _id != "x" else _id for _id in lines[1].split(",")]

    print(in_service)

    min_id = in_service[0]
    # max_id = in_service[-1]
    # id_range = len(in_service)

    # slope = int(lcm(min_id, max_id - id_range - 1))

    slopes = sorted(
        [
            get_slope(min_id, bus_id, i)
            for (i, bus_id) in enumerate(in_service)
            if bus_id != "x"
        ]
    )

    search_interval = slopes[-1] * slopes[-2]

    breakpoint()
    slope = 1
    lower = min_id
    while True:
        if lower % min_id == 0 and ((lower + id_range - 1) % max_id == 0):

            good_range = True

            for i in range(id_range):
                if in_service[i] == "x":
                    continue

                if (lower + i) % in_service[i] != 0:
                    good_range = False
                    break

            if good_range:
                break

        lower += slope

    print(lower)
