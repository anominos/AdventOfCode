with open("d08in.txt") as f:
    a = map(int,f.read().strip().split())
a = list(a)
#a = list(map(int, "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split()))
def dfs(a, p2=False):
    childs, meta = a[0], a[1]
    i=2
    c=[]
    for z in range(childs):
        di, metaSum = dfs(a[i:], p2)
        c.append(metaSum)
        i+=di
    if p2 and c!=[]:
        return i+meta, sum([c[i-1] if i <= len(c) else 0 for i in a[i:i+meta]])
    else:
        return i+meta, sum(a[i:i+meta])+sum(c)
print(dfs(a)[1])
print(dfs(a, p2=True)[1])