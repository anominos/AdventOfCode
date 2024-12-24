# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

state = {}
import re
def func(x):
    return [*map(int, re.findall(r"-?\d+",x)),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    a, b = f.read().split("\n\n")

    for x in a.split("\n"):
        if x!="":
            n, i = x.split(": ")
            state[n] = bool(int(i))

from collections import *
import numpy as np
import math
from utils import *

DIAG_DIRS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # Clockwise from north for (i,j): l[di][dj]
ADJ_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NESW for (i, j): l[di][dj]

def do(a, b, c):
    if c == "AND":
        return a and b
    if c=="OR":
        return a or b
    if c=="XOR":
        return a != b
b = b.split("\n")

gates = {}

for x in b:
    if x:
        g = re.match(r"(\S+) (AND|OR|XOR) (\S+) -> (\S+)", x)
        i1, oper, i2, o = (g.groups())
        gates[o] = (i1, i2, oper)

def get(s):
    if s in state:
        return state[s]
    a, b, c = gates[s]
    if a not in state:
        state[a] = get(a)
    if b not in state:
        state[b] = get(b)
    state[s] = do(state[a], state[b], c)
    return state[s]

i = 0
ans = 0
while f"z{i:02}" in gates or f"z{i:02}" in state:
    ans += get(f"z{i:02}") * (1<<i)
    # print(int(state[f"z{i:02}"]), f"z{i:02}")
    i+=1

print(ans)
# print(i)
# state = {}

# def getpath(s):
#     if s in gates:
#         a, b, c = gates[s]
#         return (getpath(a), getpath(b), c)
#     else:
#         return s

# backgates = {((a,b,c) if a<b else (b,a,c)):i for i,(a,b,c) in gates.items()}
# def find(s):
#     a, b, c = s
#     if a<b:
#         return backgates[a,b,c]
#     else:
#         return backgates[b,a,c]


# s = find(("x00", "y00", "XOR"))
# c = find(("x00", "y00", "AND"))

# def equal(a, b):
#     if a in gates:
#         return equal(gates[a], b)
#     if b in gates:
#         return equal(a, gates[b])
#     if type(a) == str and type(b) == str:
#         return a == b
#     if type(a) == str or type(b) == str:
#         return False
#     x1, y1, op1 = a
#     x2, y2, op2 = b
#     return (
#         (op1==op2) and equal(x1, x2) and equal(y1, y2)
#         or (op1==op2) and equal(x1, y2) and equal(y1, x2)
#     )

# correct = {"z00"}
# seen = {c}

# def pathcorrect(s):
#     correct.add(s)
#     if s in seen:
#         seen.remove(s)
#     if s in gates:
#         a, b, _ = gates[s]
#         pathcorrect(a)
#         pathcorrect(b)

# def pathseen(s):
#     if s in correct:
#         return
#     seen.add(s)
#     if s in gates:
#         a, b, _ = gates[s]
#         pathseen(a)
#         pathseen(b)

for bit in range(1, i):
    code = f"{bit:02}"
    z = "z"+code
    x = "x"+code
    y = "y"+code
    if gates[z][-1] != "XOR":
        print(z, gates[z])

for k, (i1,i2,op) in gates.items():
    if op == "OR":
        if gates[i1][-1] == "XOR":
            print(k, i1)
        if gates[i2][-1] == "XOR":
            print(k, i2)

l = ["rts","z07",
"jpj","z12",
"kgj","z26",
"vvw","chv",
]

print(*sorted(l), sep=",")

"""
rts,z07
jpj,z12
kgj,z26
vvw,chv


"""


    # xxory = find((x, y, "XOR"))
    # xandy = find((x, y, "AND"))

    # nexts = find((xxory, c, "XOR"))
    # xxoryandc = find((xxory, c, "AND"))
    # nextc = find((xandy, xxoryandc, "OR"))


    # targs = ((x, y, "XOR"), getpath(c), "XOR")

    # if equal(getpath(z), targs):
    #     pathcorrect(z)
    #     pathcorrect(c)


    # targc = (((x, y, "XOR"), getpath(c), "AND"), (x, y, "AND"), "OR")

    # if equal(targc)

    # if not equal(getpath(nextc), targc):
    #     print(nextc)
    #     break

# print(getpath("z00"))
# print(getpath("z01"))
# print(getpath("qkf"))
# print(getpath("z02"))
# print(getpath("z07"))
# print(len(gates))