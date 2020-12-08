import math

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
            return r[0] * 8 + c[0]


def ans2(seats):
    for i in range(len(seats)):
        if seats[i] + 1 < seats[i+1]:
            return seats[i] + 1


seats = []
for ticket in tickets:
    seats.append(ans1(ticket))

seats = sorted(set(seats))

sseats = []
for seat in seats:
    sseats.append(seat)

# ans1:
print(max(seats))
# ans2:
print(ans2(sseats))
