*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []
import re
def func(x):
    return [*map(int, re.findall(r"-?\d+",x)),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

for x in l:
