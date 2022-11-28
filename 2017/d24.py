from collections import defaultdict
d= defaultdict(list)
with open("d24in.txt") as f:
    for x in f:
        a, b = map(int,x.strip().split("/"))
        d[a].append(b)
        d[b].append(a)
maxx = 0
max2 = (0,0)
todo = [(0,(0,), set())]
while todo != []:
    cur = todo.pop()
    strength, path, done = cur
    for x in d[path[-1]]:
        if not (y:=(min(path[-1], x), max(path[-1], x))) in done:
            new = path+(x,)
            newstr = strength + path[-1] + x
            newdone = done|{y}
            todo.append((newstr, new, newdone))
            maxx = max(maxx, newstr)
            max2 = max(max2, (len(new), newstr))
print(maxx)
print(max2[1])
# >1114