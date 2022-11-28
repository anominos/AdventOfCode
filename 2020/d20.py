dat = []
with open("d20in.txt") as f:
    for x in f.read().split("\n\n"):
        dat.append((x.strip()))

d = {}
from collections import defaultdict
d2 = defaultdict(list)
for x in dat:
    x = x.splitlines()
    n = int(x[0].split()[1][:-1])
    x = x[1:]
    d[n] = x
    for y in [x[0], x[-1], "".join([i[0] for i in x]), "".join([i[-1] for i in x])]:
        d2[y].append(n)
        d2[y[::-1]].append(n)
from collections import Counter
c = Counter()
for x in d.values():
    for y in [x[0], x[-1], "".join([i[0] for i in x]), "".join([i[-1] for i in x])]:
        if y[::-1] in c.keys():
            y = y[::-1]
        c[y]+=1
f = Counter()
for x, y in c.items():
    if y==1:
        f[d2[x][0]]+=1
m=1
corner = []
for x,y in f.items():
    if y==2:
        m*=x
        corner.append(x)
print(m)
def getAdj(x):
    ##up right down left
    return [x[0], "".join([i[-1] for i in x]), x[-1], "".join([i[0] for i in x])]

adjs = [[0,-1], [1, 0], [0, 1], [-1, 0]]

coords = {}
done = set()
first = d[corner[0]][:]
for _ in range(8):
    if _%2==0:
        first = list(map("".join, zip(*first)))
    else:
        first = first[::-1]
    a = getAdj(first)
    b = [d2[i] for i in a]
    if len(b[1])==2 and len(b[2])==2:
        o = _
        break
todo = [[corner[0], o, 0, 0]]
while todo:
    cur, o, posx, posy = todo.pop()
    done.add(cur)
    # print(posx, posy,o, cur)
    part = d[cur][:]

    for _ in range(o+1):
        if _%2==0:
            part = list(map("".join, zip(*part)))
        else:
            part = part[::-1]
    coords[posx, posy] = part
    for i,x in enumerate(getAdj(part)):
        adj = d2[x][:]
        adj.remove(cur)
        if adj!=[]:
            adj = adj[0]
            # print(i, x, adj)
            if not adj in done:
                #find orien
                #then add todo
                agr = d[adj][:]
                for j in range(8):
                    if j%2==0:
                        agr = list(map("".join, zip(*agr)))
                    else:
                        agr = agr[::-1]
                    if x == getAdj(agr)[(i+2)%4]:
                        break
                dx, dy = adjs[i]
                todo.append([adj, j, posx+dx, posy+dy])




def removeAdj(a):
    return [i[1:-1] for i in a[1:-1]]

# print(coords[0,0])
grid = []
leny = len(coords[0,0])-2
for y in range(0,max(coords.keys(), key=lambda a:a[1])[1]+1):
    for _ in range(leny):
        grid.append("")
    for x in range(0, max(coords.keys())[0]+1):
        for i,z in enumerate(removeAdj(coords[x, y])):
            grid[-leny+i]+=z

monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.splitlines()
c=0
d=0
while c==0:
    c=0
    if d%2==0:
        grid = list(map("".join, zip(*grid)))
    else:
        grid= grid[::-1]
    for y in range(len(grid)-len(monster)):
        for x in range(len(grid[y])-len(monster[0])):
            f=True
            for dy in range(len(monster)):
                for dx in range(len(monster[0])):
                    if monster[dy][dx] == "#" and grid[y+dy][x+dx]!="#":
                        f=False
            if f:
                c+=1
    if c!=0:
        print("".join(grid).count("#")-("".join(monster).count("#") * c))
    d+=1

# < 1954