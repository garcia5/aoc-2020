import subprocess
import time

EMPTY = ".L"
OCCUPIED = "#"


def replace_at_pos(line, new, idx):
    return line[:idx] + str(new) + line[idx + 1 :]


def simulate(_state):

    HEIGHT = len(state)
    WIDTH = len(state[0])
    start_state = _state.copy()

    while True:
        end_state = start_state.copy()
        subprocess.call("clear")
        print("\n".join(start_state))

        for i in range(HEIGHT):
            for j in range(WIDTH):

                if start_state[i][j] == ".":
                    continue

                col = "".join([row[j] for row in start_state])
                row = start_state[i]

                neighbors = []

                # if i == 1 and j == 1:
                # breakpoint()

                # look right
                for s in row[j + 1 :]:
                    if s != ".":
                        neighbors.append(s)
                        break

                # look left
                for _j in range(j - 1, -1, -1):
                    s = row[_j]
                    if s != ".":
                        neighbors.append(s)
                        break

                # down
                for s in col[i + 1 :]:
                    if s != ".":
                        neighbors.append(s)
                        break

                # up
                for _i in range(i - 1, -1, -1):
                    s = col[_i]
                    if s != ".":
                        neighbors.append(s)
                        break

                _i = i - 1
                _j = j - 1
                while _i >= 0 and _j >= 0:
                    s = start_state[_i][_j]
                    if s != ".":
                        neighbors.append(s)
                        break
                    _i -= 1
                    _j -= 1

                _i = i + 1
                _j = j - 1
                while _i < HEIGHT and _j >= 0:
                    s = start_state[_i][_j]
                    if s != ".":
                        neighbors.append(s)
                        break
                    _i += 1
                    _j -= 1

                _i = i + 1
                _j = j + 1
                while _i < HEIGHT and _j < WIDTH:
                    s = start_state[_i][_j]
                    if s != ".":
                        neighbors.append(s)
                        break
                    _i += 1
                    _j += 1

                _i = i - 1
                _j = j + 1
                while _i >= 0 and _j < WIDTH:
                    s = start_state[_i][_j]
                    if s != ".":
                        neighbors.append(s)
                        break
                    _i -= 1
                    _j += 1

                occupied_count = sum([1 for o in neighbors if o == OCCUPIED])

                if occupied_count >= 5:
                    end_state[i] = replace_at_pos(end_state[i], "L", j)

                elif occupied_count == 0:
                    end_state[i] = replace_at_pos(end_state[i], "#", j)

        # breakpoint()
        if start_state == end_state:
            return end_state

        start_state = end_state.copy()


def occupied_count(grid):
    total = 0
    for line in grid:
        total += sum([1 for s in line if s == OCCUPIED])

    return total


if __name__ == "__main__":
    state = [l.strip() for l in open("input", "r")]
    steady_state = simulate(state)
    print(occupied_count(steady_state))
