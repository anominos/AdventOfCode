with open("d06in.txt") as f:
    f = [i.strip() for i in f]
    cols = [[] for i in f[0]]
    for x in f:
        for y in range(len(x)):
            cols[y].append(x[y])
print("silver:","".join(map(lambda a:max(a, key=a.count), cols)))
print("gold:","".join(map(lambda a:min(a, key=a.count), cols)))
