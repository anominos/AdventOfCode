# flake8: noqa

*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

from collections import *
import numpy as np
import math


s = re.findall(r"mul\((\d+),(\d+)\)", "".join(l))
c=0
for a,b in s:
    c+=int(a)*int(b)
print(c)


s = re.findall(r"((mul)\((\d+),(\d+)\))|((do(n't)?)\(\))", "".join(l))
c=0
enabled = True
for i in s:
    if "mul" in i and enabled:
        c+=int(i[2])*int(i[3])
    elif "do" in i:
        enabled = True
    elif "don't" in i:
        enabled = False
print(c)