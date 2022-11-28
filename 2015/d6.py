ins = []
with open("d6in.txt") as f:
    for x in f:
        ins.append(x)

lights = [[False]*1000 for _ in range(1000)]
import re
p = re.compile("(\d+)")
for x in ins:
    state = 0
    if "on" in x:state=1
    elif "off" in x:state =2
    a, b, c, d = re.findall(p, x)
    for y in range(int(b), int(d)+1):
        for x in range(int(a), int(c)+1):
            if state==0:
                lights[y][x] = not(lights[y][x])
            elif state == 1:
                lights[y][x] = True
            else:
                lights[y][x] = False
c=0
for x in lights:
    c+=sum(x)
print(c)

del lights
lights = [[0]*1000 for _ in range(1000)]
import re
p = re.compile("(\d+)")
for x in ins:
    state = 2
    if "on" in x:state=1
    elif "off" in x:state =-1
    a, b, c, d = re.findall(p, x)
    for y in range(int(b), int(d)+1):
        for x in range(int(a), int(c)+1):
            lights[y][x]=max(0, lights[y][x]+state)
c=0
for x in lights:
    c+=sum(x)
print(c)