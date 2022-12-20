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
            l.append(int(x))
# from collections import deque
# l = deque(l)
# for start in l.copy():
#     l.rotate(-l.index(start))
#     # print(l[-1], l[0], l[1])
#     l.popleft()
#     l.rotate(-(start))
#     l.appendleft(start)
#     # print(l[-1], l[0], l[1])
#     # input()
l = list(enumerate(l))
g = l.copy()
for start in g:
    i = l.index(start)
    del l[i]
    i = (i+start[1])%len(l)
    l.insert(i, start)
    # print(l)
e = [i[1] for i in l]
z=e.index(0)
a,b,c = z+1000,z+2000,z+3000
a%=len(e)
b%=len(e)
c%=len(e)
print(e[a]+e[b]+e[c])
dkey = 811589153
l = [[i, j*dkey] for (i,j) in g]
g = [[i,j] for i,j in l]
for _ in range(10):
    for start in g:
        i = l.index(start)
        del l[i]
        i = (i+start[1])%len(l)
        l.insert(i, start)
e = [i[1] for i in l]
z=e.index(0)
a,b,c = z+1000,z+2000,z+3000
a%=len(e)
b%=len(e)
c%=len(e)
print(e[a]+e[b]+e[c])
