f = open("d16in.txt")
l = f.read().strip().split(",")
f.close()

def run(d):
    for x in l:
        if x[0] == "s":
            amount = len(d)-int(x[1:])
            d = d[amount:]+d[:amount]
        elif x[0] == "x":
            a, b = map(int,x[1:].split("/"))
            d[a], d[b] = d[b], d[a]
        elif x[0] == "p":
            a,b = map(d.index,x[1:].split("/"))
            d[a], d[b] = d[b], d[a]
    return d

print("".join(run(list(map(lambda a:chr(a+ord("a")), range(16))))))

d = list(map(lambda a:chr(a+ord("a")), range(16)))
past = []
while not tuple(d) in set(past):
    past.append(tuple(d))
    d = run(d)
num = int(1e9)
n = num%len(past)
print("".join(past[n]))
