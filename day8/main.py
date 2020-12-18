lines = []
with open("input") as f:
    lines = [line.strip().split() for line in f.readlines()]

instructions = [w[0] for w in lines]
values = [int(w[1]) for w in lines]


def ans1(insts, values):
    acc, i = 0, 0
    steps = set()
    while True:
        if i in steps:
            return (False, acc)
        elif i == len(lines):
            return(True, acc)
        steps.add(i)
        inst = insts[i]
        value = values[i]
        if inst == "acc":
            acc += int(value)
        if inst == "jmp":
            i += int(value)
        else:
            i += 1


def ans2(insts, values):
    to_change = (i for i, x in enumerate(insts) if x in ('nop', 'jmp'))
    for i in to_change:
        new_instructions = list(insts)
        new_instructions[i] = "jmp" if insts[i] == 'nop' else 'nop'
        halts, acc = ans1(new_instructions, values)
        if halts:
            _, acc = ans1(new_instructions, values)
            break
    return(acc)


_, acc = ans1(instructions, values)
print(acc)
print(ans2(instructions, values))
