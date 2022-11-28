def a(tf):
    players = 446
    maxx = 71522*(100**tf)
    scores =[0]*players
    from collections import deque
    marbles = deque([0])
    curplay = 0
    for a in range(maxx):
        marbles.rotate(-1)
        if a%23==22:
            scores[curplay] += a+1
            marbles.rotate(8)
            scores[curplay]+=marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.append(a+1)

        curplay+=1
        curplay%=players
    print(max(scores))
a(False)
a(True)