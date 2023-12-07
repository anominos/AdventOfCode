*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return x.split()

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

c_order = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")
w = []
from collections import Counter
def comp1(a: str):
    if len(set(a)) == 1:
        return 0
    elif len(set(a)) == 2:
        if a.count(a[0]) in [1, 4]:
            return 1
        else:
            return 2
    else:
        a = Counter(a)
        if max(a.values()) == 3:
            return 3
        elif list(a.values()).count(2) == 2:
            return 4
        elif max(a.values()) == 2:
            return 5
        else:
            return 6

w = sorted(l, key=lambda a: (comp1(a[0]), *tuple(c_order.index(i) for i in a[0])), reverse=True)
c=0
for i, x in enumerate(w, start=1):
    c+= i * int(x[1])
print(c)

c_order = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")

def comp2(b: str):
    l = 100
    for i in c_order[:-1]:
        a = b.replace("J", i)
        l = min(l, comp1(a))
    return l

w = sorted(l, key=lambda a: (comp2(a[0]), *tuple(c_order.index(i) for i in a[0])), reverse=True)
c=0
for i, x in enumerate(w, start=1):
    c+= i * int(x[1])
print(c)