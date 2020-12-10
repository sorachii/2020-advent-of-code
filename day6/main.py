lines = []
with open("input") as f:
    for line in f:
        lines.append(line.strip())

lines.append("")


def ans1():
    total, grp = 0, set()
    for line in lines:
        prs = set(line)
        if prs:
            grp.update(prs)
        else:
            total += len(grp)
            grp = set()
    return total


def ans2():
    total, grp = 0, None
    for line in lines:
        prs = set(line)
        if prs:
            if grp is None:
                grp = prs
            else:
                grp.intersection_update(prs)
        elif grp is not None:
            total += len(grp)
            grp = None
    return total


print(ans1())
print(ans2())
