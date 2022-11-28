with open("d01in.txt") as f:
    inp = f.read().strip().split(", ")
prev = [[0,0]]
pos = [0,0]
d = [0,1]
gold = None
for x in inp:
    dis = int(x[1:])
    d = d[::-1]
    if d[0]==0:
        if x[0]=="R":
            d[1]=-d[1]
    elif x[0]=="L":
        d[0]=-d[0]
    for _ in range(dis):
        pos = [pos[0]+d[0], pos[1]+d[1]]
        if pos in prev and gold==None:
            gold = sum(map(abs, pos))
        prev.append(pos)
        

print("silver:",sum(map(abs, pos)))
print("gold:", gold)