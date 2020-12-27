import re

import numpy as np

with open("input") as f:
    ls = [line.strip() for line in f.readlines()]

ranges = [list(map(int, re.findall('\d+', x))) for x in ls[:19]]
your = np.array([int(x) for x in ls[22].split(',')], dtype=np.int64)
nearby = [list(map(int, re.findall('\d+', x))) for x in ls[25:]]

valid = set()
for t1, t2, t3, t4 in ranges:
    valid |= set(range(t1, t2+1))
    valid |= set(range(t3, t4+1))

# Answer 1
print(sum(n for l in nearby for n in l if n not in valid))
