import re

pattern = re.compile(r'(\d+)-(\d+) (\w): (\w*)', re.A)

lista = []

with open('input') as f:
    for line in f:
        lista.append(line)

def parse(line):
    lo, hi, char, string = re.match(pattern, line).groups()
    return int(lo), int(hi), char, string

def ans1():
    count = 0
    for line in lista:
        lo, hi, char, string = parse(line)
        if string.count(char) in range(lo, hi + 1):
            count += 1
    return count

print(ans1())
