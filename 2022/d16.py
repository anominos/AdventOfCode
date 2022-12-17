*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []
import re
def func(x):
    return re.findall(r"-?\d+|[A-Z][A-Z]",x)
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))
start = "AA"
from collections import defaultdict
graph = defaultdict(list)
index = defaultdict(int)
flow = {}
g=0
for x in l:
    if int(x[1]) != 0:
        index[x[0]] = 1<<g
        g += 1
    flow[x[0]] = int(x[1])
    for y in x[2:]:
        graph[x[0]].append(y)

# dp = defaultdict(lambda:[[0]*(30) for _ in range(1<<g)])
from functools import lru_cache
@lru_cache(maxsize=None)
def dfs(cur, opened, tleft):
    if tleft<=0:
        return 0
    if opened+1 == 1<<g:
        return 0
    mx=0
    if flow[cur]>0 and not opened&(index[cur]):
        mx = dfs(cur, opened|(index[cur]), tleft-1) + flow[cur]*tleft
    for x in graph[cur]:
        mx = max(mx, dfs(x, opened, tleft-1))
    return mx

def dfs2(cur, ele, opened=0, tleft=25):
    if tleft<=0:
        return 0
    if (opened|r)+1 == 1<<len(index):
        return 0
    open_cur = opened, 0
    open_ele = opened, 0
    if not opened&(1<<index[cur]):
        open_cur = opened|(1<<index[cur]), flow[cur]*tleft
    if cur!=ele:
        if not opened&(1<<index[ele]):
            open_ele = opened|(1<<index[ele]), flow[ele]*tleft
    mx = 0
    for x in range(-1, len(graph[cur])):
        for y in range(-1, len(graph[ele])):
            nxt = [graph[cur][x], graph[ele][y], opened, tleft-1, 0]
            if x==-1:
                if open_cur[1] == 0:
                    continue
                nxt[0] = cur
                nxt[2] |= open_cur[0]
                nxt[-1] += open_cur[1]
            if y==-1:
                if open_ele[1] == 0:
                    continue
                nxt[1] = ele
                nxt[2] |= open_ele[0]
                nxt[-1] += open_ele[1]
            if nxt[0] > nxt[1]:
                nxt[0], nxt[1] = nxt[1], nxt[0]
            mx = max(mx, dfs2(*nxt[:-1]) + nxt[-1])
    # print(cur, bin(opened), tleft, mx)
    return mx

print(dfs("AA", opened=0, tleft=29))
# for opened in range(1<<g):
#     dfs("AA", opened=opened, tleft=25)

mx=0
for i in range(1, 1<<g):
    for j in range(i, 1<<g):
        if i|j==(1<<g)-1:
            b = dfs("AA", opened=i, tleft=25) + dfs("AA", opened=j, tleft=25)
            mx=max(mx, b)
print(mx)
