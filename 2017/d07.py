weights = {}
childs = {}
with open("d07in.txt") as f:
    for x in f:
        r = x.strip().split(" -> ")
        if len(r)!=1:
            cur, ch = r
            ch = ch.split(", ")
        else:
            cur = r[0]
            ch = []
        key, weight = cur.split()
        weight = int(weight[1:-1])
        weights[key] = weight
        childs[key] = ch
class Node:
    def __init__(self, key="", weight=0, children=[]):
        self.key = key
        self.children = children
        self.weight = weight

keys = list(weights.keys())
done = set()
l = {}
def dfs(a, l):
    if not a in done:
        if childs[a]==[]:
            l[a] = Node(a, weights[a])
        else:
            d=[]
            for x in childs[a]:
                l = dfs(x, l)
                d.append(l[x])
                del l[x]
            l[a] = Node(a, weights[a], d)
    done.add(a)
    return l

for x in keys:
    l = dfs(x, l)
for x in l.values():
    root = x

def dfs2(node):
    if node.children ==[]:
        node.totWeight = node.weight
        return node.weight
    w = node.weight
    for x in node.children:
        w+=dfs2(x)
    node.totWeight = w
    return w
dfs2(root)
def dfs3(node):
    l = list(map(lambda a:a.totWeight, node.children))
    odd = min(l, key=l.count)
    norm = max(l, key=l.count)
    if odd==norm:
        return node.weight

    for x in node.children:
        if x.totWeight==odd:
            rt = dfs3(x)
            if type(rt)==int:
                return rt, norm-odd
            return rt
a, b = (dfs3(root))
print(a+b)