from collections import defaultdict

path = ""
with open("d20in.txt") as f:
    path = f.read().strip()
# path = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
path = path.replace("|", ")(")
dirs = [[0,-1],[-1,0],[0,1],[1,0]]
names = "NWSE"
dname = dict(zip(names, dirs))
path = path[1:-1]
d = defaultdict(list)
def rec(i, x, y):
    while i < len(path):
        if path[i] == "(":
            i = rec(i+1, x, y)
        elif path[i] == ")":
            return i
        else:
            dx, dy = dname[path[i]]
            d[x, y].append(path[i])
            d[x+dx, y+dy].append(names[(names.index(path[i])+2)%4])
            x+=dx
            y+=dy
        i+=1

rec(0, 0, 0)

todo = {(0,0)}
done = set()
c=0
c2=0
while todo:
    if c>=1000:
        c2+=len(todo)
    new = set()
    for i in todo:
        done.add(i)
        curx, cury = i
        for n in d[i]:
            dx, dy = dname[n]
            if (y:=(curx+dx, cury+dy)) not in done:
                new.add(y)
    c+=1
    todo = new
print(c-1)
print(c2)

# xx = min(d.keys())[0]
# yy = min(d.keys(), key=lambda a:a[1])[1]
# a = [["#"]*11 for _ in range(11)]
# for x in d:
#     nx, ny = (x[0]-xx)*2+1, (x[1]-yy)*2+1
#     a[ny][nx] = "."
#     for i in d[x]:
#         dx, dy = dname[i]
#         a[ny+dy][nx+dx] = "|" if dx!=0 else "-"
    
# for x in a:
#     print(*x, sep="")

#<5137