# Thinking about revisiting this and
# solving it with itertools.combinations for practice
lines = []
with open("input") as f:
    nums = [int(line) for line in f.readlines()]


def ans1(nums):
    for i, n in enumerate(nums):
        if i < 25:                  # preamble
            continue
        prev = nums[i-25:i]
        if not any(n == n1 + n2 for n1 in prev for n2 in prev):
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
