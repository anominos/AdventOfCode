*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return [eval(x.split()[0]), eval(x.split()[1])]

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n\n"):
        if x!="":
            l.append(func(x))


def check(i, j):
    if type(i)==int and type(j)==int:
        if i!=j:
            return i<j
    else:
        if type(i)==int:
            i = [i]
        elif type(j)==int:
            j = [j]
        for a,b in zip(i, j):
            if check(a,b) is not None:
                return check(a, b)
        if len(i) < len(j):
            return True
        elif len(i) > len(j):
            return False
c=0
for i, (x,y) in enumerate(l, start=1):
    if check(x,y):
        c+=i
print(c)
l = sum(l, start=[])
l.append([[2]])
l.append([[6]])

from functools import cmp_to_key

l.sort(key=cmp_to_key(lambda a,b: 1 if check(a, b) else -1), reverse=True)
print((l.index([[2]])+1)*(l.index([[6]])+1))
