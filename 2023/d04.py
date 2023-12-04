*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    return [*map(int, re.findall(r"-?\d+",x))]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            a, b = x.split("|")
            l.append((set(func(a)[1:]), set(func(b))))

c=0
from collections import Counter
c2 = Counter()

for (i, (a, b)) in enumerate(l, start=1):
    if len(a&b)>0:
        c += 2**(len(a&b)-1)
    r = len(a&b)
    c2[i] += 1
    for a in range(1, r+1):
        c2[i+a] += c2[i]
print(c)
print(sum(c2.values()))