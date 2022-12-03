import re
from collections import Counter

*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []

def func(x):
    # return [*map(int, re.findall(r"-?\d+", x))]
    return x


with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

print(len(l))
c=0
for i in range(0, len(l), 3):
    x = l[i]
    a,b = x[:len(x)//2], x[len(x)//2:]
    d1 = Counter(a), Counter(b)
    d = Counter(x)
    for z in range(1,3):
        d &= Counter(l[i+z])

    for x in d:
        if x.islower():
            c += ord(x) - ord("a") + 1
        else:
            c += ord(x) - ord("A") + 27

print(c)
