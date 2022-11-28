silver = 0
gld = 0
with open("d03in.txt") as f:
    gt = [[],[],[]]
    for x in f:
        a,b,c = map(int,x.strip().split())
        gt[0].append(a)
        gt[1].append(b)
        gt[2].append(c)
        a,b,c = sorted([a,b,c])
        if a+b>c:
            silver+=1

        if len(gt[0])==3:
            for z in gt:
                if sum(z)-max(z)>max(z):
                    gld+=1
            gt = [[],[],[]]

print("silver:",silver)
print("gold:",gld)