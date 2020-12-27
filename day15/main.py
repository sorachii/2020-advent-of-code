from collections import defaultdict
from itertools import count

nums = [12, 1, 16, 3, 11, 0]
tnums = [0, 3, 6]


def ans1(iteration):
    d = defaultdict(list)
    for i in count(1):
        if i <= len(nums):
            new = nums[i-1]
        elif len(d[last_spoken]) == 1:
            new = 0
        else:
            new = d[last_spoken][-1] - d[last_spoken][-2]
        if i == iteration:
            return new
        d[new].append(i)
        last_spoken = new


print(ans1(2020))
print(ans1(30000000))
