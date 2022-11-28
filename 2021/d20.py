from collections import defaultdict


dat = []
with open("d20in.txt") as f:
    for x in f.read().split("\n\n"):
        dat.append(x.strip())

iea = dat[0].replace("\n", "")
img = dat[1]
img = img.splitlines()
imgg = defaultdict(bool)
for i,x in enumerate(img):
    for j,y in enumerate(x):
        imgg[j,i] = y=='#'

from itertools import product
# print(iea[int("100110001",2)])
k = lambda a:a[1]
for t in range(50):
    # print(not(t&1))
    nw = defaultdict(lambda a=t:a%2==0)
    # print(imgg[-500,-500])
    # del imgg[-500,-500]
    # nw = defaultdict(bool)
    xs = list(range(min(imgg.keys())[0]-1, max(imgg.keys())[0]+2))
    ys = list(range(min(imgg.keys(), key=k)[1]-1, max(imgg.keys(),key=k)[1]+2))
    # l=[]
    # for y in ys:
    #     c=""
    #     for x in xs:
    #         c+=".#"[imgg[x,y]]
    #     l.append(c)
    # print("\n".join(l))
    # print()

    for x,y in product(xs,ys):
        s = ""
        for dy,dx in product(range(-1,2),repeat=2):
            s+="01"[imgg[x+dx,y+dy]]
        # print(s,x,y)
        nw[x,y] = iea[int(s,2)]=="#"
    # print(imgg)
    imgg = nw
    # print(imgg)
    if t==1:print(sum(1 for i in filter(None, imgg.values())))

print(sum(1 for i in filter(None, imgg.values())))


# xs = list(range(min(imgg.keys())[0]-1, max(imgg.keys())[0]+2))
# ys = list(range(min(imgg.keys(), key=k)[1]-1, max(imgg.keys(),key=k)[1]+2))
# l=[]
# for y in ys:
#     c=""
#     for x in xs:
#         c+=".#"[imgg[x,y]]
#     l.append(c)
# print("\n".join(l))
# print()