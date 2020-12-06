count = 0
answers = []

for l in open('input', 'r'):
    l = l.strip()
    print(l)

    if len(l) == 0:
        common = answers[0]
        for p in answers[1:]:
            common = common & p

        count += len(common)
        answers = []

    else:
        answers.append(set([c for c in l]))

common = answers[0]
for p in answers[1:]:
    common = common & p

count += len(common)

print(count)
