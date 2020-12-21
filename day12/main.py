with open("input") as f:
    lines = [line.strip() for line in f.readlines()]


data = [(line[0], int(line[1:])) for line in lines]


def ans1(data):
    dirs = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}
    rot = {'L': 1j, 'R': -1j}
    loc = 0
    d = 1
    for act, value in data:
        if act in dirs:
            loc += dirs[act] * value
        elif act in rot:
            d *= rot[act] ** (value/90)
        else:
            loc += d * value

    return(abs(loc.real) + abs(loc.imag))


print(ans1(data))
