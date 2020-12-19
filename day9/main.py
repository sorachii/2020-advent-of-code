lines = []
with open("input") as f:
    nums = [int(line) for line in f.readlines()]


def ans1(nums):
    for i, n in enumerate(nums):
        if i < 25:                  # 25 == preamble
            continue
        prev = nums[i-25:i]
        if not any(n == n1 + n2 for n1 in prev for n2 in prev):
            return(n)


print(ans1(nums))
