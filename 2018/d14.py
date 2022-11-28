from time import time
ttt = time()
pin = 880751
comp = list(map(int, str(pin)))
score = [3,7]
cur = [0,1]
p2 = -1
p1 = -1
while p2==-1 or p1 == -1:
    new = score[cur[0]]+score[cur[1]]
    for x in str(new):
        score.append(int(x))
        if score[-6:]==comp:
            p2 = len(score)-6
    cur[0] = (cur[0]+1+score[cur[0]])%len(score)
    cur[1] = (cur[1]+1+score[cur[1]])%len(score)
    if len(score) > pin+10 and p1==-1:
        p1 = "".join(map(str, score[pin:pin+10]))   
print(p1)
print(p2)
# print(time()-ttt)