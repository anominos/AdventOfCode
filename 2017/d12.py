d={}
with open("d12in.txt") as f:
    for x in f:
        a,b = x.strip().split(" <-> ")
        d[int(a)] = list(map(int,b.split(", ")))
f=True
c=0
nums = set(range(max(d.keys())))
while nums!=set():
    todo = {nums.pop()}
    done = set()
    while todo!=set():
        n = todo.pop()
        done.add(n)
        for x in d[n]:
            if not x in done:
                todo.add(x)
    if f:
        print(len(done))
        f=False
    nums -= done
    c+=1
print(c)