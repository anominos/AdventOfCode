class Node:
    def __init__(self,name):
        self.child = []
        self.par = []
        self.name = name
        self.time = ord(name) - ord("A") + 61
    def unlock(self,prevs):
        return set(map(lambda a:a.name, self.par)).issubset(set(prevs))
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name

d = {}
with open("d07in.txt") as f:
    for x in f:
        n = x.split()
        source, dest = n[1], n[-3]
        for r in [source, dest]:
            if d.get(r, None) == None:
                d[r] = Node(r)
        d[source].child.append(d[dest])
        d[dest].par.append(d[source])

start = []
for x in d:
    if d[x].par == []:
        start.append(x)

order = ""
while start!=[]:
    cur = min(start)
    start.remove(cur)
    order+=cur
    for i in d[cur].child:
        if i.unlock(order):
            start.append(i.name)
print(order)
done = []
avail = []
for x in d:
    if d[x].par == []:
        avail.append(x)


workers = [None]*5
c=0
first = True
while not(workers == [None]*len(workers) and avail==[]):
    for i,x in enumerate(workers):
        if x != None:
            x.time-=1
            if x.time==0:
                done.append(x.name)
                for j in x.child:
                    if j.unlock(done):
                        avail.append(j.name)
                workers[i] = None
        if workers[i]==None:
            if avail!=[]:
                workers[i] = d[min(avail)]
                avail.remove(min(avail))
    if workers != [None]*len(workers):c+=1
print(c)