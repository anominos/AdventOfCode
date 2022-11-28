with open("d12in.txt") as f:
    a = f.read().strip()

import re
print(sum(map(int, re.findall(r"(-?\d+)", a))))

c = eval(a)

def dfs(x):
    s=0
    if type(x)==list:
        for y in x:
            s+=dfs(y)
    elif type(x)==dict:
        if all(y!="red" for y in x.values()):
            for y in x.values():
                s+= dfs(y)
    elif type(x)==int:
        return x
    return s

print(dfs(c))