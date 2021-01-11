import re
from lark import Lark

with open('input') as f:
    data = f.read()

rules, messages = data.split('\n\n')
messages = messages.split()

def solve(rules):
    rules = 'start: t0\n' + re.sub(r'(\d+)', r't\1', rules)
    parser = Lark(rules)
    valid = len(messages)
    for message in messages:
        try:
            parser.parse(message)
        except:
            valid -= 1
    return valid

print(solve(rules))
