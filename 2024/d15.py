# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return list((x))

with open(f"{a}/input/{b}.txt") as f:
    a, b = f.read().split("\n\n")
    for x in a.split("\n"):
        if x!="":
            l.append(func(x))

from collections import *
import numpy as np
import math
from utils import *

DIAG_DIRS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # Clockwise from north for (i,j): l[di][dj]
ADJ_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NWSE for (i, j): l[di][dj]


moves = b
grid = [i[:] for i in l]
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == "@":
            pos = x, y


cx, cy = pos
dirs = list("^>v<")
for m in moves:
    if m=="\n":continue
    dx, dy = ADJ_DIRS[dirs.index(m)]
    nx, ny = cx, cy
    while grid[nx][ny] in "O@":
        nx += dx
        ny += dy

    if grid[nx][ny] == ".":
        grid[nx][ny] = grid[cx+dx][cy+dy]
        grid[cx+dx][cy+dy] = grid[cx][cy]
        grid[cx][cy] = "."
        cx += dx
        cy += dy
c=0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == "O":
            c += 100 * x + y
print(c)

#####################

moves = b
grid = []
for x in a.split("\n"):
    if x!="":
        grid.append(list(x.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")))

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == "@":
            pos = x, y


def can_push(cx, cy, dx):
    if grid[cx+dx][cy] == ".":
        return True
    elif grid[cx+dx][cy] == "#":
        return False
    elif grid[cx+dx][cy] == "[":
        return can_push(cx+dx, cy, dx) and can_push(cx+dx, cy+1, dx)
    elif grid[cx+dx][cy] == "]":
        return can_push(cx+dx, cy, dx) and can_push(cx+dx, cy-1, dx)


def push(cx, cy, dx):
    if grid[cx+dx][cy] == "[":
        push(cx+dx, cy, dx)
        push(cx+dx, cy+1, dx)
    elif grid[cx+dx][cy] == "]":
        push(cx+dx, cy, dx)
        push(cx+dx, cy-1, dx)
    grid[cx+dx][cy] = grid[cx][cy]
    grid[cx][cy] = "."

cx, cy = pos
dirs = list("^>v<")
for m in moves:
    if m=="\n":continue
    dx, dy = ADJ_DIRS[dirs.index(m)]
    if dy==0:
        if can_push(cx, cy, dx):
            push(cx, cy, dx)
            # grid[cx][cy] = "."
            cx += dx
            cy += dy
    else:
        nx, ny = cx, cy

        while grid[nx][ny] in "[]@":
            nx += dx
            ny += dy

        if grid[nx][ny] == ".":
            while (nx, ny) != (cx, cy):
                grid[nx][ny] = grid[nx-dx][ny-dy]
                nx -= dx
                ny -= dy
            grid[cx][cy] = "."
            cx += dx
            cy += dy

c=0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == "[":
            c += 100 * x + y
print(c)