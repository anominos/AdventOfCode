*a, b = __file__.split("\\")
b = b.split(".")[0]
a = "\\".join(a)

l = []
import re
def func(x):
    # return [*map(int, re.findall(r"-?\d+",x)),]
    return str((x))

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x!="":
            l.append(func(x))
d = {}
i=0
cur_d = d
stack = []
while i < len(l):
    if l[i][0] == "$":
        cmds = l[i].split()[1:]
        if cmds[0] == "cd":
            if cmds[1] == "/":
                cur_d = d
            elif cmds[1] == "..":
                cur_d = stack.pop()
            else:
                cur_d[cmds[1]] = cur_d.get(cmds[1], {})
                stack.append(cur_d)
                cur_d = cur_d[cmds[1]]
            i+=1
        elif cmds[0] == "ls":
            i+=1
            while i<len(l) and l[i][0] != "$":
                r = l[i].split()
                if r[0] == "dir":
                    cur_d[r[1]] = cur_d.get(r[1], {})
                else:
                    cur_d[r[1]] = int(r[0])
                i+=1
    else:
        print("HI")

cc=0
mn = 99999999999999999
def rec(d, t=None):
    global cc, mn
    if type(d) == int:
        return d
    c=0
    for i,j in d.items():
        c+=rec(j, t)
    if c<=1_00_000:
        cc += c
    if t is not None:
        if c >= t:
            mn = min(mn, c)
    return c
tot = rec(d)
print(cc)

rec(d, 30000000-(70000000 - tot))
print(mn)
