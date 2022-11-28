MOD = 20183
depth = 7740
targ = (12,763)

# depth = 510
# targ = (10,10)



d = {}
def getGI(x, y):
    if (x,y)==targ:
        d[x,y] = 0
        return 0
    if (x, y) in d.keys():
        return d[x, y]
    if x==0:
        d[x,y] = (y*48271 + depth)%MOD
        return d[x,y]
    if y==0:
        d[x,y] = (x*16807 +depth) % MOD
        return d[x, y]
    d[x,y] = (getGI(x-1, y)*getGI(x, y-1) + depth) % MOD
    return d[x, y]
c=0
for y in range(targ[1]+1):
    for x in range(targ[0]+1):
        if (x, y)==targ:continue
        c+=getGI(x, y)%3
    #     print(end=".=|"[((getGI(x, y)+depth)%20183)%3])
    # print()
print(c)
#neither:0, torch:1, climb:2 
from struc import PriorityQueue
from collections import defaultdict
def getType(x, y):
    return getGI(x,y)%3

adj = [[0,1],[0,-1],[-1,0],[1,0],[0,0]]

dist = defaultdict(lambda:float("inf"))
dist[(0,0,1)] = 0
q = PriorityQueue()
visited = set()
end = targ+(1,)
q.add((0,0,1), 0)
while not end in visited:
    u = q.pop()
    visited.add(u)
    x, y, tool = u
    for dx, dy in adj:
        ds = 1
        if (dx, dy)==(0,0):
            tool = 3 - tool - getType(x,y)
            ds = 7
        v = (x+dx, y+dy, tool)
        if v[0] >= 0 and v[1] >= 0 and tool != getType(v[0],v[1]) and not v in visited:
            path = ds+dist[u]
            if path < dist[v]:
                dist[v] = path
                q.add(v, path) 

            

print(dist[targ[0],targ[1],1])

# print(dist)
# cur = (targ[0], targ[1],1)
# while (y:= prev[cur])!=None:
#     print(y)
#     cur = y
#     c+=1

