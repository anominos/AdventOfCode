start = ".^^^^^.^^.^^^.^...^..^^.^.^..^^^^^^^^^^..^...^^.^..^^^^..^^^^...^.^.^^^^^^^^....^..^^^^^^.^^^.^^^.^^"
##start = ".^^.^.^^^^"
##size = 10

def run(size):
    prev = []
    for x in start:
        prev.append(x=="^")
    tot = 0
    for _ in range(size-1):

        tot += prev.count(False)
        prev = [False]+prev+[False]
        new = []
        for i in range(len(start)):
            l,r = prev[i], prev[i+2]
            new.append(l!=r)
        prev = new[:]

    tot += prev.count(False)

    print(tot)
from time import time

run(40)
ttt=time()
run(400000)
print(time()-ttt)