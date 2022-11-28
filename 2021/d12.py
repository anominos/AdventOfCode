dat = []
with open("d12in.txt") as f:
    for x in f:
        dat.append((x.strip()))

from collections import defaultdict, deque,Counter
d = defaultdict(list)
for x in dat:
    a,b = x.split("-")
    d[a].append(b)
    d[b].append(a)

def dfs(cur, counts = Counter()):
    if cur == "end":
        return 1
    c=0
    for x in d[cur]:
        if x=="start":continue
        if x.lower()==x and counts[x]>=1:
            continue
        counts[x]+=1
        c+= dfs(x,counts)
        counts[x]-=1
    return c
print(dfs("start"))





d = defaultdict(list)
for x in dat:
    a,b = x.split("-")
    d[a].append(b)
    d[b].append(a)

def dfs(cur, counts = Counter()):
    if cur == "end":
        return 1
    c=0
    for x in d[cur]:
        if x=="start":continue
        if any(x==x.lower() and y >= 2 for x,y in counts.items()) and x.lower()==x and counts[x]==1:
            continue
        if x.lower()==x and counts[x]>=2:
            continue
        counts[x]+=1
        c+= dfs(x,counts)
        counts[x]-=1
    return c
print(dfs("start"))
