a = []
with open("d02in.txt") as f:
    for x in f:
        a.append(x.strip())

from collections import Counter
two = 0
three = 0
for x in a:
    t = th = False
    for let, count in Counter(x).items():
        if count==2:
            t=True
        elif count==3:
            th=True
    two+=t
    three+=th
print(two*three)
def main(a):
    a =set(a)
    for x in a:
        for y in range(len(x)):
            for let in "qwertyuiopasdfghjklzxcvbnm":
                z = list(x)
                if let != z[y]:
                    z[y] = let
                    if (b:="".join(z)) in a:
                        print(b[:y]+b[y+1:])
                        return
main(a)