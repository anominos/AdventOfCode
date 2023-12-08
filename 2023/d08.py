*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    return [*re.findall(r"[A-Z1-9]{3}",x)]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    a, b = f.read().split("\n\n")
    for x in b.split("\n"):
        if x!="":
            l.append(func(x))

d = {}
for x, y, z in l:
    d[x] = (y, z)


i = 0
cur = "AAA"
while cur != "ZZZ":
    cur = d[cur][a[i%len(a)] == "R"]
    i+=1
print(i)


curs = [i for i in d.keys() if i[-1] == "A"]
l = []
for s in curs:
    i = 0
    while s[-1] != "Z":
        s = d[s][a[i%len(a)] == "R"]
        i+=1
    l.append(i)
from math import gcd
n = 1
for x in l:
    n = x * n // gcd(x, n)


# visited = {"AAA"}
# def search(node, cur_s):
#     # print(node)
#     visited.add(node)
#     if node == "ZZZ":
#         return cur_s
#     else:
#         if d[node][0] not in visited and (x:=search(d[node][0], cur_s+"L")) is not None:
#             return x
#         elif d[node][1] not in visited and (x:=search(d[node][1], cur_s+"R")) is not None:
#             return x
#         else:
#             return None

# # print(len(search("AAA", "")))