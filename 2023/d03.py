*a, b = __file__.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return list((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))

c = 0
def symbol(s):
    if s in "1234567890":
        return False
    if s==".":
        return False
    return True

def get_adj(x, y, l):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if 0<= x+dx < len(l) and 0<= y+dy < len(l[x]):
                yield (x+dx, y+dy)

from collections import defaultdict
d = defaultdict(list)

for x in range(len(l)):
    cur_num = 0
    good = False
    g = set()
    for y in range(len(l[x])):
        if l[x][y].isdigit():
            cur_num = cur_num * 10 + int(l[x][y])
            for nx, ny in get_adj(x, y, l):
                if symbol(l[nx][ny]):
                    good = True
                if l[nx][ny] == "*":
                    g.add((nx, ny))
        else:
            if good:
                c+=cur_num
                # print(cur_num)
            for i in g:
                d[i].append(cur_num)
            cur_num = 0
            good = False
            g = set()
    if good:
        c+=cur_num
        # print(cur_num)
        for i in g:                 # Forgot these two lines lol
            d[i].append(cur_num)    #
    cur_num = 0
print(c)

# print(dict(d))
c2 = 0
for i, j in d.items():
    if l[i[0]][i[1]] != "*":
        print(i)
    if len(j) != 1:
        c2 += j[0]*j[1]

print(c2)