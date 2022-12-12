*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    a,b,c,d,e,f = str(x).strip().split("\n")
    a = [*map(int, re.findall(r"-?\d+",a)),][0]
    b = [*map(int, re.findall(r"-?\d+",b)),]
    c = eval(c.split(":")[1].replace("new =", "lambda old:"))
    d = [*map(int, re.findall(r"-?\d+",d)),][0]
    e = [*map(int, re.findall(r"-?\d+",e)),][0]
    f = [*map(int, re.findall(r"-?\d+",f)),][0]
    return a,b,c,d,e,f


with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n\n"):
        if x!="":
            l.append(func(x))

from collections import defaultdict

monkeys = []
for a, b, *_ in l:
    monkeys.append(b[:])
inspected = defaultdict(int)
for turn in range(20):
    for a,b,c,d,e,f in l:
        for wry in monkeys[a]:
            cw = (c(wry)//3)
            inspected[a] +=1
            if cw%d==0:
                monkeys[e].append(cw)
            else:
                monkeys[f].append(cw)
        monkeys[a] = []

a,b = sorted(inspected.values(), reverse=True)[:2]
print(a*b)
MOD = 1
monkeys = []
for a, b, _, d, *_ in l:
    monkeys.append(b)
    MOD *= d
inspected = defaultdict(int)
for turn in range(10000):
    for a,b,c,d,e,f in l:
        for wry in monkeys[a]:
            cw = (c(wry))%MOD
            inspected[a] +=1
            if cw%d==0:
                monkeys[e].append(cw)
            else:
                monkeys[f].append(cw)
        monkeys[a] = []
a,b = sorted(inspected.values(), reverse=True)[:2]
print(a*b)
