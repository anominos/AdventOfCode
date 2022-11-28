twos = {}
threes = {}
with open("d21in.txt") as f:
    for x in f:
        a, b = x.strip().split(" => ")
        b = b.split("/")
        a = a.split("/")
        if len(a)==2:
            twos[tuple(a)] = b
        if len(a)==3:
            threes[tuple(a)] = b
start = """.#.
..#
###""".split("\n")
for _ in range(18):
    if len(start)%2==0:
        new = []
        for y in range(0,len(start),2):
            new.extend([""]*3)
            for x in range(0,len(start),2):
                z=(start[y][x:x+2], start[y+1][x:x+2])
                n=0
                while not z in twos.keys():
                    z=tuple(map("".join, zip(*z[::-1])))
                    n+=1
                    if n==4:
                        z=z[::-1]
                for i,x in enumerate(twos[z]):
                    new[i-3]+=x
    else:
        new = []
        for y in range(0,len(start),3):
            new.extend([""]*4)
            for x in range(0, len(start),3):
                z=(start[y][x:x+3], start[y+1][x:x+3], start[y+2][x:x+3])
                n=0
                while not z in threes.keys():
                    z=tuple(map("".join, zip(*z[::-1])))
                    if n==4:
                        z=z[::-1]
                    n+=1
                for i,x in enumerate(threes[z]):
                    new[i-4]+=x

    start= new[:]
    if _==4:
        c=0
        for x in new:
            c+=x.count("#")
        print(c)
c=0
for x in new:
    c+=x.count("#")
print(c)
    