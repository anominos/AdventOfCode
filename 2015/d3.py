from collections import defaultdict
a = defaultdict(int)
b = defaultdict(int)
adj = [[1,0],[0,1],[-1,0],[0,-1]]
dr = ">v<^"
with open("d3in.txt") as f:
    for x in f:
        s=x
    pos = [0,0]
    pos2 = [0,0]
    pos3 = [0,0]
    a[(0,0)]=1
    t=True
    for x in s:
        if t:
            p=pos
        else:
            p=pos2
        t = not(t)
        dx, dy = adj[dr.index(x)]
        p[0]+=dx
        p[1]+=dy
        pos3[0]+=dx
        pos3[1]+=dy
        b[tuple(pos3)]+=1
        a[tuple(p)]+=1
print(len(b))
print(len(a))