lines = []
with open("input") as f:
    for line in f:
        lines.append(line.split())


def ans1(operations):
    acc = 0
    i = 0
    steps = set()
    while i < len(operations) and i not in steps:
        if operations[i][0] == "nop":
            steps.add(i)
            i += 1
        elif operations[i][0] == "acc":
            steps.add(i)
            acc += int(operations[i][1])
            i += 1
        elif operations[i][0] == "jmp":
            steps.add(i)
            i += int(operations[i][1])
    return acc


print(ans1(lines))
