from collections import defaultdict

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


def ans2(jrs):
    paths = defaultdict(int)
    paths[0] = 1
    for i in range(1, len(jrs)):
        for j in range(i)[::-1]:
            if jrs[i] - jrs[j] > 3:
                break
            paths[i] += paths[j]
    return(paths[len(jrs)-1])


print(ans1(jrs))
print(ans2(jrs))
