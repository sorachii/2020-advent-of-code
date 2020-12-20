from collections import Counter, defaultdict

with open("input") as f:
    jrs = [int(jr) for jr in f.readlines()]
jrs = [0] + sorted(jrs) + [max(jrs) + 3]


def ans1(jrs):
    diffs = []
    for i, _ in enumerate(jrs):
        if i+1 < len(jrs):
            diff = jrs[i+1] - jrs[i]
            diffs.append(diff)
        elif i == len(jrs):
            diff = jrs[i] - jrs[i-1]
            diffs.append(diff)
        else:
            return diffs.count(1) * diffs.count(3)


print(ans1(jrs))
