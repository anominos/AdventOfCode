# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
from types import TracebackType
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return x.split("\n")

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().strip().split("\n\n"):
        if x!="":
            l.append(func(x))

from collections import *
import numpy as np
import math
from utils import *

DIAG_DIRS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # Clockwise from north for (i,j): l[di][dj]
ADJ_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NESW for (i, j): l[di][dj]

shapes = l[:6]
boxes = l[6:][0]

shapes = [i[1:] for i in shapes]

shape_coords = []
get_shape = {}
for i, shape in enumerate(shapes):
    for _ in range(4):
        shape_coords.append(frozenset((i,j) for i in range(len(shape)) for j in range(len(shape[i])) if shape[i][j] == "#"))
        get_shape[shape_coords[-1]] = i
        shape = GridFunc.rotate_grid(shape)
    flip_shape = shape[::-1]
    for _ in range(4):
        shape_coords.append(frozenset((i,j) for i in range(len(flip_shape)) for j in range(len(flip_shape[i])) if flip_shape[i][j] == "#"))
        get_shape[shape_coords[-1]] = i
        flip_shape = GridFunc.rotate_grid(flip_shape)



shape_perimeter = {}
for shape in shape_coords:
    shape_perimeter[shape] = set()
    for (i, j) in shape:
        for di, dj in DIAG_DIRS:
            if (i+di, j+dj) not in shape:
                shape_perimeter[shape].add((i+di, j+dj))
    shape_perimeter[shape] = frozenset(shape_perimeter[shape])



def shift_shape(coord, shape):
    for c in shape:
        yield c[0]+coord[0], c[1]+coord[1]

def fits(coord, shape, filled):
    for i in shift_shape(coord,shape):
        if i in filled:
            return False
    return True

def fittable(n, m, perimeter, filled, shapesleft):
    assert isinstance(perimeter, frozenset)
    assert isinstance(filled, frozenset)
    if sum(shapesleft) == 0:
        return True
    for x in perimeter:
        for shape in shape_coords:
            if shapesleft[get_shape[shape]] == 0:
                continue
            bad = False
            for y in shape:
                if not(0<=x[0]+y[0]<n and 0<=x[1]+y[1]<m):
                    bad = True
                    break
            if bad:
                continue

            if fits(x, shape, filled):
                shapesleft[get_shape[shape]] -= 1
                if fittable(
                    n,
                    m,
                    perimeter | frozenset(shift_shape(x, shape_perimeter[shape])),
                    filled | frozenset(shift_shape(x, shape)),
                    shapesleft
                ):
                    return True
                shapesleft[get_shape[shape]] += 1
    return False

dd=0
for x in boxes:
    a, b, *c = map(int, re.findall(r"-?\d+",x))
    if sum(c) * 8 < a*b:
        dd += 1
    # if fittable(a, b, frozenset([(0, 0)]), frozenset(), c):
    #     print(x)
print(dd)
"""
 a a
a#a#a
a#a#a
a###a
 aaa

"""