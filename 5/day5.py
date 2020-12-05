max_id = 0
min_id = 999
seen = []

to_int = lambda bstr: int(''.join(['1' if c in ['B', 'R'] else '0' for c in bstr]), 2)

for l in open('input', 'r'):
    l = l.strip()
    id = (to_int(l[:7]) * 8) + to_int(l[7:])
    seen.append(id)

    if id > max_id: max_id = id
    if id < min_id: min_id = id

for id in range(min_id, max_id):
    if id not in seen:
        print(id)
