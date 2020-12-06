count = 0
answers = {}

for l in open('input', 'r'):
    l = l.strip()
    print(l)

    if len(l) == 0:
        count += len(answers.keys())
        answers = {}

    answers.update({w: 1 for w in l})

count += len(answers.keys())
print(count)
