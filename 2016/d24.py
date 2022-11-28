import re
nums = []
inp = []
with open("d24in.txt") as f:
    for x in f:
        nums.extend(re.findall("\d", x))
        inp.append(x.strip())

starts = {}
for y in range(len(inp)):
    for x in range(len(inp[y])):
        if inp[y][x] in  nums:
            starts[inp[y][x]] =((x,y), 0, ((inp[y][x],0),))

def bfs(start):
    todo = [starts[start]]
    done = set()
    adj = [[0,1], [1,0], [0,-1], [-1,0]]
    a=  []
    while todo!=[]:
        neww = []
        for cur in todo:
            (curx, cury), dis, path = cur
            done.add((curx, cury))
            t=True
            for newx,newy in adj:
                if not((curx+newx, cury+newy) in done) and (sq:=inp[cury+newy][curx+newx])!= "#":
                    if sq in nums:
                        neww.append(((curx+newx, cury+newy), 0, path+((sq, dis+1),)))
                    else:
                        neww.append(((curx+newx, cury+newy), dis+1, path))
                    t=False

            if t and path!=((start,0),):a.append(path)
        todo = list(set(neww))
    return a

n = {}
for x in nums:
    n[x] = list(map(lambda a:a[1:], set(bfs(x))))
for x, y in n.items():
    n[x]= list(map(lambda a:a[0], filter(lambda a:len(a)==1, y)))


from itertools import permutations
def find(l, i):
    for x in l:
        if x[0]==i:
            return x

def solve(f):
    minn = float("inf")
    for x in permutations(range(7)):
        cur = "0"
        dis = 0
        if f:
            x+=(-1,)
        for y in x:
            y = str(y+1)
            cur, d = find(n[cur], y)
            dis+=d
        minn = min(minn, dis)
    return (minn)

print(solve(False))
print(solve(True))
#filter(lambda a:len(a)==1,[(('0', 12),), (('0', 12), ('5', 42)), (('3', 220),), (('0', 12), ('7', 48)), (('6', 186),), (('4', 68),), (('1', 216),)])