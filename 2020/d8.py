dat = []
with open("d8in.txt") as f:
    for x in f:
        dat.append(x.strip())

def run(dat):
    acc = 0
    i=0
    prev = set()
    while i < len(dat):
        code, rand = dat[i].split()
        if i in prev:
            return False
        prev.add(i)
        rand = int(rand)
        if code=="acc":
            acc+=rand
        if code=="jmp":
            i+=rand-1
        i+=1
    return acc

for i in range(len(dat)):
    c, r = dat[i].split()
    cpy = dat[:]
    # if c=="nop":
    #     cpy[i] = "jmp "+r
    if c=="jmp":
        cpy[i] = "nop "+r
        if y:=run(cpy):
            print(y)
            break