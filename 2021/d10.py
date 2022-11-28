dat = []
with open("d10in.txt") as f:
    for x in f:
        dat.append((x.strip()))


pair = dict(zip(")>]}","(<[{"))
d = dict(zip(")>]}", [3,25137, 57, 1197]))
c=0
valid = []
for x in dat:
    stack = []
    e = 0
    for y in x:
        if y in "(<[{":
            stack.append(y)
        else:
            if stack.pop() != pair[y]:
                e = d[y]
                # print(x, stack)
                break
    if e==0:
        valid.append(x)

    c+=e
print(c)

p = dict(zip("([{<", range(1,5)))
scores = []
for x in valid:
    stack = []
    for y in x:
        if y in "([{<":
            stack.append(y)
        else:
            stack.pop()
    s = 0
    for n in stack[::-1]:
        s*=5
        s+=p[n]
    scores.append(s)
print(sorted(scores)[len(scores)//2])

