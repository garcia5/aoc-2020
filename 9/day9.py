history = []
history_len = 25
magic_num = 731031916
# magic_num = 43
s = []


def is_sum(s):
    if sum(s) == magic_num:
        print('got sum!', s)
        print(min(s))
        print(max(s))
        print(f'min + max = {min(s) + max(s)}')
        return True


for line in open('input', 'r'):

    line = int(line.strip())

    if line == magic_num:
        print('got to magic num with no subset found')
        break

    s.append(line)

    while sum(s) > magic_num:
        s.pop(0)

    if is_sum(s):
        break
