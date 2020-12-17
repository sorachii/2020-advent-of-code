lines = []
with open("input.sample") as f:
    for line in f:
        lines.append(line.split())


def ans1(operations):
    acc, i = 0, 0
    steps = set()
    while True:
        if i in steps:
            return (False, acc)
        elif i == len(lines):
            return(True, acc)
        steps.add(i)
        if operations[i][0] == "nop":
            i += 1
        elif operations[i][0] == "acc":
            acc += int(operations[i][1])
            i += 1
        elif operations[i][0] == "jmp":
            i += int(operations[i][1])


def ans2(operations):
    to_change = (i for i, inst in enumerate(operations) if inst[0] in ('nop', 'jmp'))
    acc, i = 0, 0
    steps = set()
    for i in to_change:
        new_instructions = list(operations)
        print(new_instructions[i][0])
        new_instructions[i][0] = "jmp" if operations[i][0] == 'nop' else 'nop'
        halts, acc = ans1(new_instructions)
        if halts:
            break
    return(acc)


print(ans1(lines))
print(ans2(lines))
