l=[]
with open("d25in.txt") as f:
    for x in f:
        l.append(list(map(int, x.strip().split(","))))
from collections import defaultdict
graph = defaultdict(list)

for x in range(len(l)):
    for y in range(len(l)):
        if x!=y:
            if sum(abs(l[x][i]-l[y][i]) for i in range(4))<=3:
                graph[x].append(y)


c=0
a = [-1]*len(l)


def dfs(i):
    if a[i] == 0:
        return
    a[i] = 0
    for x in graph[i]:
        dfs(x)

for i,x in enumerate(a):
    if x==-1:
        dfs(i)
        c+=1


print(c)