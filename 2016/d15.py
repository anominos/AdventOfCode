import re
pat = re.compile("Disc #\d has (\d+) positions; at time=0, it is at position (\d).")

for c in range(2):
    l= []
    for x in open("d15in.txt"):
        l.append(re.match(pat,x).groups())
    if c==1:
        l.append((11, 0))
    #l = [(5, 4), (2, 1)]
    step = 1
    tot = 0
    for x in range(len(l)):
        size, startPos = map(int, l[x])
        finPos = size-x-1

        curPos = (startPos+tot)%size
        while curPos != finPos:
            tot +=step
            curPos = (curPos+step)%size
        step *= size
    print("gold:" if c else "silver:", tot)