dat = []
with open("d4in.txt") as f:
    for x in f.read().split("\n\n"):
        dat.append((x.strip()))


deck = dat[0].split(",")
boards = dat[1:]
marked = []
for x in range(len(boards)):
    a = [i.split() for i in boards[x].split("\n")]
    boards[x] = a
    marked.append([[False]*5 for _ in range(5)])

def find(i,l):
    for y in range(5):
        for x in range(5):
            if l[y][x] == i:
                return x,y
    return -1,-1
o = None
d = len(boards)
s = set()
for x in deck:
    for g in range(len(boards)):
        if g in s:
            if len(s)==1:
                if o!=None:
                    c=0
                    # print(o, marked[g])
                    for y in range(5):
                        for n in range(5):
                            if not m[y][n]:
                                c+= int(o[y][n])
                    # print(c)
                    print(c*int(f))
                s.add(-1)
            continue
        a,b = find(x, boards[g])
        if (a,b) == (-1,-1):
            continue
        marked[g][b][a] = True
        if any(map(all, marked[g])):
            o = boards[g]
            m = marked[g]
            f = x
            s.add(g)
        elif any(map(all, zip(*marked[g][::-1]))):
            o = boards[g]
            m = marked[g]
            f = x
            s.add(g)
        # print(marked[g], list(zip(*marked[g][::-1])))
# print(o,m)
if o!=None:
    c=0
    # print(o, marked[g])
    for y in range(5):
        for n in range(5):
            if not m[y][n]:
                c+= int(o[y][n])
    # print(c)
    print(c*int(f))
    

    