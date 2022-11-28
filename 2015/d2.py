tot = 0
tot2 = 0
with open("d2in.txt") as f:
    for x in f:
        a, b, c = map(int, x.split("x"))
        tot+= 2*a*b + 2*c*b + 2*a*c
        tot+=min([a*b, b*c, a*c])
        tot2 += 2*(sum([a,b,c])-max([a,b,c]))
        tot2+=a*b*c
print(tot)
print(tot2)