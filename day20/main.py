from itertools import product
from math import prod

import networkx as nx
import numpy as np

with open('input') as f:
    data = f.read().strip()

blocks = data.split('\n\n')

mats = {}
for b in blocks:
    b = b.splitlines()
    n = int(b[0][5:9])
    mat = np.array([[c == '#' for c in l] for l in b[1:]])
    mats[n] = mat


def symmetries(mat):
    for _ in range(4):
        yield mat
        yield np.flipud(mat)
        mat = np.rot90(mat)


def match(mat1, mat2):
    for mat in symmetries(mat2):
        if(mat1[0] == mat[-1]).all():
            return (-1, 0), mat
        if(mat1[-1] == mat[0]).all():
            return (1, 0), mat
        if(mat1[:, -1] == mat[:, 0]).all():
            return (0, 1), mat
        if(mat1[:, 0] == mat[:, -1]).all():
            return (0, -1), mat


# First part
G = nx.Graph()
for (i1, mat1), (i2, mat2) in product(mats.items(), repeat=2):
    if i1 > i2 and match(mat1, mat2):
        G.add_edge(i1, i2)

print(prod(k for k, v in G.degree() if v == 2))
