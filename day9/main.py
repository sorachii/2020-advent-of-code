from itertools import combinations


lines = []
with open("input") as f:
    nums = [int(line) for line in f.readlines()]


def ans1(nums):
    for i, n in enumerate(nums):
        if i < 25:                  # preamble
            continue
        prev = nums[i-25:i]
        combs = list(combinations(prev, 2))
        if not any(n == sum(tup) for tup in combs):
            return(n)


def ans2(nums):
    for size in range(2, len(nums)):
        for i in range(len(nums) - size):
            s = nums[i:i+size]
            if sum(s) == invalid:
                return(min(s) + max(s))


invalid = ans1(nums)
print(invalid)
print(ans2(nums))
