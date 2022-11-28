dat = []
import re
with open("d18in.txt") as f:
    for x in f:
        dat.append(eval(x.strip()))

class node:
    def __init__(self, par=None, left=None, right=None):
        self.par = par
        self.left = left
        self.right = right
        self.depth = -1
        self.mx = -1
    
    def __repr__(self):
        return f"[{str(self.left)} {str(self.right)}]"

def create(a,b):
    n = node()
    if type(a)==int:
        n.left=a
    else:
        n.left = create(*a)
        n.left.par = n
    if type(b)==int:
        n.right = b
    else:
        n.right = create(*b)
        n.right.par = n
    return n

def depths(r,d=0):
    if type(r)==int:
        return 0
    r.depth = max(depths(r.left), depths(r.right))
    return r.depth+1

def mxs(r):
    if type(r)==int:
        return r
    r.mx = max(mxs(r.left),mxs(r.right))
    return r.mx

def explode(r):
    cur = r
    while cur.depth>=1:
        if type(cur.left) != int and cur.left.depth == cur.depth-1:
            cur = cur.left
        else:
            cur = cur.right
    try:
        lft = cur
        while lft.par.left == lft:
            lft = lft.par
        lft = lft.par
        if type(lft.left) == int:
            lft.left = lft.left+cur.left
        else:
            lft = lft.left
            while type(lft.right)!=int:
                lft = lft.right
            lft.right = lft.right+cur.left
    except AttributeError:
        pass
    try:
        rgt = cur
        while rgt.par.right == rgt:
            rgt = rgt.par
        rgt = rgt.par
        if type(rgt.right) == int:
            rgt.right = rgt.right+cur.right
        else:
            rgt = rgt.right
            while type(rgt.left)!=int:
                rgt = rgt.left
            rgt.left = rgt.left + cur.right
    except AttributeError as e:
        pass
    if cur.par.left == cur:
        cur.par.left = 0
    else:
        cur.par.right = 0
    
    # upd = cur.par
    # while upd.par != None:
    #     upd = upd.par
    #     uld = upd.left
    #     if type(uld)==int:
    #         uld = 0
    #     else:uld=uld.depth
    #     urd =upd.right
    #     if type(urd)==int:
    #         urd = 0
    #     else:urd=urd.depth
    #     upd.depth = max(uld, urd)+1


def split(r):
    cur = r
    left = True
    while True:
        if type(cur.left) == int:
            if cur.left >= 10:
                break
            elif type(cur.right)==int:
                left =False
                break
            else:
                cur = cur.right
        elif type(cur.right)==int:
            if cur.left.mx>=10:
                cur=cur.left
            else:
                left=False
                break
        else:
            if cur.left.mx >= 10:
                cur = cur.left
            else:
                cur = cur.right
    
    if left:
        cur.left = node(left=cur.left//2, right = cur.left//2 + cur.left%2)
        cur.left.par= cur
    else:
        cur.right = node(left=cur.right//2, right = cur.right//2+cur.right%2)
        cur.right.par = cur

root = create(*dat[0])
for x in range(len(dat)-1):
    a = create(*dat[x+1])
    n = node()
    a.par = n
    root.par = n
    n.left = root
    n.right = a
    root = n
    depths(root)
    mxs(root)
    while root.depth >= 4 or root.mx >=10:
        if root.depth >= 4:
            explode(root)
        elif root.mx >= 10:
            split(root)
        depths(root)
        mxs(root)
        # print(root)
    # print("OUT", root)
    # input()

def mag(cur):
    l = cur.left
    if type(cur.left) != int:
        l=mag(cur.left)
    r=cur.right
    if type(cur.right)!= int:
        r=mag(cur.right)
    return 3*l + 2*r
print(mag(root))
mx = 0
for x in range(len(dat)):
    for y in range(len(dat)):
        if x==y:continue
        a = create(*dat[x])
        b = create(*dat[y])
        root = node(left=a,right=b)
        a.par = root
        b.par = root
        depths(root)
        mxs(root)
        while root.depth >= 4 or root.mx >=10:
            if root.depth >= 4:
                explode(root)
            elif root.mx >= 10:
                split(root)
            depths(root)
            mxs(root)
        mx = max(mx, mag(root))
print(mx)

# cur = dat[0]
# for x in range(len(dat)-1):
#     cur = f"[{cur}, {dat[x+1]}]"
#     cur = explodes(cur)

        