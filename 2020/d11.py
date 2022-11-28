dat = []
with open("d11in.txt") as f:
    for x in f:
        dat.append(list(x.strip()))
prev = []
adjs = [(i,j) for i in range(-1, 2) for j in range(-1, 2) if not(i==j==0)]
t=True
d=0
while t:
    d+=1
    t = False
    new = []
    for x in range(len(dat)):
        new.append([])
        for y in range(len(dat[x])):
            c=0
            for dx, dy in adjs:
                nx, ny = x, y
                nx+=dx
                ny+=dy
                while 0<=nx<len(dat) and 0<=ny<len(dat[x]):
                    if dat[nx][ny]=="L":break
                    if dat[nx][ny]=="#":
                        c+=1
                        break
                    nx+=dx
                    ny+=dy
            # print(c, x, y)
            if dat[x][y]=="L":
                if c==0:
                    new[x].append("#")
                    t = True
                else:
                    new[x].append("L")
            elif dat[x][y] == "#":
                if c>=5:
                    new[x].append("L")
                    t =True
                else:
                    new[x].append("#")
            else:
                new[x].append(".")
    dat = new
    # for x in dat:
    #     print("".join(x))
    # print()
print(d)
c=0       
for x in dat:
    c+=x.count("#")
print(c)
