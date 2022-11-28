dat = []
with open("d2in.txt") as f:
    for x in f:
        dat.append((x.strip()))

h,d = 0,0
for x in dat:
    x = x.split()
    # print(x)
    if x[0] == "forward":
        h+= int(x[1])
    elif x[0] == "up":
        d-=int(x[1])
    else:
        d+=int(x[1])

print(h*d)

h,d = 0,0
aim=0
for x in dat:
    x = x.split()
    # print(x)
    if x[0] == "forward":
        h+= aim*int(x[1])
        d+=int(x[1])
    elif x[0] == "up":
        aim-=int(x[1])
    else:
        aim+=int(x[1])

print(h*d)