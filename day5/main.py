import math
import cProfile
# First seven always halfs the airplane's 128(0-127) rows
# FBFBBFF - RLR
# F = lower half
# B = upper half
# Start by considering the whole range, rows 0 through 127.
"""
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
"""

"""
char:   low:    high:   keep:
        0       127     l
F       0       63      h
B       32      63      l
F       32      47      h
B       40      47      h
B       44      47      l
F       44      45      l
F       44      44
"""

# Last 3 characters halfs the airplane's 8 columns
# L = lower half
# R = upper half

"""
t = []
with open(input) as f:
    for i in f:
        t.append(i)
"""

with open('input') as f:
    tickets = [line.strip() for line in f]

rmin, rmax = 0, 127
cmin, cmax = 0, 7


def ans1(ticket):
    r = [rmin, rmax]
    c = [cmin, cmax]
    for i, char in enumerate(ticket):
        if ticket[i] == "F":
            r[1] = math.floor((r[1]+r[0])/2)
        if ticket[i] == "B":
            r[0] = math.ceil((r[1]+r[0])/2)
        if ticket[i] == "R":
            c[0] = math.ceil((c[0]+c[1])/2)
        if ticket[i] == "L":
            c[1] = math.floor((c[0]+c[1])/2)
        if c[0] == c[1]:
            return r[0] * 8 + 5


def ans2(seats):
    for i, seat in enumerate(seats):
        if seats[i] + 8 != seats[i+1]:
            return seats[i] + 8


seats = []
for ticket in tickets:
    seats.append(ans1(ticket))

print(max(seats))
