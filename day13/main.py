#!/usr/bin/env python3.7
from sympy.ntheory.modular import solve_congruence


with open("input") as f:
    lines = list(f.readlines())


bus_times = [(-i, int(x)) for i, x in enumerate(lines[1].split(',')) if x != 'x']


def ans1(lines):
    n = int(lines[0])
    x = min((int(s) for s in lines[1].split(',') if s != 'x'),
            key=lambda x: (-n) % x)
    return((-n) % x * x)


def ans2(bus_times):
    return(solve_congruence(*bus_times)[0])


print(ans1(lines))
print(ans2(bus_times))
