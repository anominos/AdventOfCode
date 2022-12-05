*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n\n"):
        if x!="":
            l.append(func(x))

start = l[0]
st = [[] for _ in range(9)]
for x in start.split("\n")[:-1]:
    for i in range(0, len(x), 4):
        if x[i:i+3] != " "*3 and len(x) > i+1:
            st[i//4].append(x[i+1])

for y in st:
    y.reverse()

for inst in l[1].split("\n"):
    if inst=="":continue
    a,b,c = [*map(int, re.findall(r"-?\d+",inst)),]
    b-=1
    c-=1
    l=[]
    # print(st[b], st[c], a)
    for _ in range(a):
        l.append(st[b].pop())
    st[c].extend(reversed(l))#(st[b].pop())
for i in st:
    print(i[-1], end="")
