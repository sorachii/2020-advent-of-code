import ast

with open("input") as f:
    ls = [line.strip()for line in f.readlines()]

# Use ast to parse tokens. Manipulate operators to force evaluation order.
# A less hacky solution would be to just use a proper tokenizer like
# https://www.geeksforgeeks.org/expression-evaluation/ and set precedence
# of operators accordingly.
def evaluate(code):
    root = ast.parse(code, mode='eval')
    for node in ast.walk(root):
        if type(node) is ast.BinOp:
            node.op = ast.Add() if type(node.op) is ast.Div else ast.Mult()
    return eval(compile(root, '<string>', 'eval'))


print(sum(evaluate(l.replace('+', '/')) for l in ls))
