import re
import functools
from collections import deque

sampleTxt = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".split('\n')

LINE_RE = re.compile(r'(\w+ \w+) bags contain (.*)')
ITEM_RE = re.compile(r'(\d+) (\w+ \w+) bags?')

lines = []
with open('input') as f:
    for line in f:
        lines.append(line.strip())


sample = []
for line in sampleTxt:
    sample.append(line.strip())


def parse(lines):
    bags = {}
    for line in lines:
        bag, items = re.match(LINE_RE, line).groups()
        # sampleImput: bags[bag] = [(1, 'bright white'), (2, 'muted yellow')]
        bags[bag] = [(int(match.group(1)), match.group(2))
                     for match in re.finditer(ITEM_RE, items)]
    return bags


def ans1(lines):
    bags = parse(lines)

    # memoization makes executing code faster. New in version 3.9
    @functools.cache
    def is_gold(item):
        return any(subitem == 'shiny gold' or is_gold(subitem)
                   for _, subitem in bags.get(item, ()))
    return sum(map(is_gold, bags))


def ans2(lines):
    bags = parse(lines)
    queue = deque(bags.get('shiny gold', ()))
    total = 0
    while queue:
        count, item = queue.popleft()
        total += count
        queue.extend((count * subcount, subitem)
                     for subcount, subitem in bags.get(item, ()))
    return total


print(ans1(lines))
print(ans2(lines))
