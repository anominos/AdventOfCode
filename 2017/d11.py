pos = [0,0]
path = open("d11in.txt").read().strip().split(",")
# path = "se,sw,se,sw,sw".split(",")

names = "nw n ne se s sw".split()
coords = [[-1,0], [0,1],[1,1],[1,0],[0,-1],[-1,-1]]
d = dict(zip(names, coords))
maxx = 0
for x in path:
    cur = d[x]
    pos[0]+=cur[0]
    pos[1]+=cur[1]
    maxx = max(maxx, max(map(abs, pos)))
print(max(map(abs, pos)))
print(maxx)