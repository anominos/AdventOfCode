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

vals = [20,60,100,140,180,220]


cur_cc = 0
s = ""
ans = 0
v=1
def check():
    global s
    s += "█" if abs(v - cur_cc%40) <= 1 else " "
    if cur_cc %40==39:
        s+="\n"



for x in l:
    n = cur_cc
    if x.split()[0] == "noop":
        check()
        cur_cc+=1
        r=0
    else:
        r=int(x.split()[1])
        check()
        cur_cc += 1
        check()
        cur_cc+=1
    try:
        if n < vals[0] and cur_cc >= vals[0]:
            ans += v * vals.pop(0)
    except:
        pass
    v += r


print(ans)
print(s)
