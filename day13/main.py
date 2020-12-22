with open("input") as f:
    lines = list(f.readlines())


def ans1(lines):
    n = int(lines[0])
    x = min((int(s) for s in lines[1].split(',') if s != 'x'),
            key=lambda x: (-n) % x)
    return((-n) % x * x)


print(ans1(lines))
