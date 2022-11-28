num = 1364
dp = {}
def cell(x, y):
    if (x,y) in dp.keys():
        return dp[(x,y)]
    
    if bin(x*x + 3*x + 2*x*y + y + y*y+num).count("1")%2==0:
        dp[(x,y)]=True
        return True
    dp[(x,y)]=False
    return False

adj = [[0,1],[1,0],[0,-1],[-1,0]]

todo = {(1,1)}
done = set()
s = 0
while not((31,39) in todo):
    s+=1
    news = set()
    for x in todo:
        done.add(x)
        for d in adj:
            newpos = (x[0]+d[0], x[1]+d[1])
            if not newpos in done and cell(*newpos) and min(newpos)>=0:
                news.add(newpos)
    todo=news.copy()
    if s==51: #s==50 still has possibles in todo, so wait one to put in done
        gld = len(done)
print("silver:",s)
print("gold:",gld)