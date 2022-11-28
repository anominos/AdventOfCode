inp = []
with open("d10in.txt") as f:
    for x in f:
        inp.append(x.strip())

d = {}
ins = {}
outs = {}
todo = []
for x in inp:
    x = x.split()
    if x[0]=="value":
        bot = int(x[-1])
        if bot in d.keys():
            d[bot].append(int(x[1]))
            todo.append(bot)
        else:
            d[bot] = [int(x[1])]
    else:
        ins[int(x[1])] = [[x[5],int(x[6])], [x[-2],int(x[-1])]]

todo = list(set(todo))
while todo!=[]:
    cur = todo.pop()
    a, b = sorted(d[cur])
    if a==17 and b==61:
        print("silver:", cur)
    ins[cur][0]+=[a]
    ins[cur][1]+=[b]
    for bo, num,val in ins[cur]:
        if bo[0]=="o":
            outs[num] = val
        else:
            if num in d.keys():
                d[num].append(val)
                todo.append(num)
            else:
                d[num] = [val]
print("gold:",outs[0]*outs[1]*outs[2])