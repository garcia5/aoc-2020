def run(program):
    acc = 0
    pc = 0
    last = pc

    while pc < len(program):
        l = program[pc]["instruction"].split(" ")
        op = l[0].strip()
        val = int(l[1])

        if program[pc]["visited"]:
            return False, acc

        program[pc]["visited"] = True
        last = pc

        if op == "acc":
            acc += val
            pc += 1

        elif op == "jmp":
            pc += val

        elif op == "nop":
            pc += 1

    return True, acc

if __name__ == "__main__":
    program = [{"instruction": l.strip(), "visited": False} for l in open("input", "r")]
    val = 0

    for i, l in enumerate(program):

        # Reset to initial state
        program = [{"instruction": l.strip(), "visited": False} for l in open("input", "r")]

        if l['instruction'].startswith('jmp'):
            program[i]['instruction'] = l['instruction'].replace('jmp', 'nop')

        elif l['instruction'].startswith('nop'):
            program[i]['instruction'] = l['instruction'].replace('nop', 'jmp')

        complete, val = run(program)

        if complete:
            print('complete')
            break

    print(val)
