class rbtNode:
    RED = True
    BLACK = False
    def __init__(self, val):
        self.val= val
        self.colour = rbtNode.RED
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, node):
        if node.val > self.val:
            if self.right==None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)
        elif node.val < self.val:
            if self.left==None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)

    def remove(self):
        if self.left == None and self.right == None:
            ## delete self
            return None
        if self.left == None:
            return self.right
        if self.right == None:
            return self.left
        lowest = self.right
        if self.right.left==None:
            self.right.left = self.left
            return self.right
        while lowest.left.left!=None:
            lowest = lowest.left
        val = lowest.left.val
        lowest.left = lowest.left.remove()
        self.val=val
        return self

    def delete(self, val):
        if self.val<val:
            if self.right:
                self.right = self.right.delete(val)
            else:
                raise ValueError("Item not in tree")
        elif self.val > val:
            if self.left:
                self.left = self.left.delete(val)
            else:
                raise ValueError("Item not in tree")
        else:
            return self.remove()
        return self

    def fixTreeInsert(self, root):
        if self == root:
            self.colour = rbtNode.BLACK
            return
        ##case where node is root is done
        if self.parent.colour==rbtNode.RED:
            gp = self.parent.parent
            uncle = gp.left if gp.left != self.parent else gp.right
            if uncle != None and uncle.colour==rbtNode.RED:
                uncle.colour = rbtNode.BLACK
                self.parent.colour = rbtNode.BLACK
                gp.colour = rbtNode.RED
                gp.fixTreeInsert(root)
            else:
                ##uncle is black
                if gp.left == self.parent:
                    if self.parent.right == self:
                        self.parent.lrotate()
                    gp.rrotate()
                    gp.colour, gp.right.colour = gp.right.colour, gp.colour
                else:
                    if self.parent.left == self:
                        self.parent.rrotate()
                    gp.lrotate()
                    gp.colour, gp.left.colour = gp.left.colour, gp.colour

    def lrotate(self):
        a, b, bc, t1, t2, t3 = self.val, self.right.val, self.right.colour, self.left, self.right.left, self.right.right
        aN = rbtNode(a)
        aN.colour = self.colour
        aN.left = t1
        aN.right = t2
        aN.parent = self
        self.val = b
        self.colour = bc
        self.left = aN
        self.right = t3

    def rrotate(self):
        a, b, bc, t1, t2, t3 = self.val, self.left.val, self.left.colour, self.right, self.left.right, self.left.left
        aN = rbtNode(a)
        aN.colour = self.colour
        aN.right = t1
        aN.left = t2
        self.val = b
        self.colour = bc
        self.right = aN
        self.left = t3
        
    
    def __repr__(self):
        return f"{'BR'[self.colour]}{self.val}:({repr(self.left)}, {repr(self.right)})"


class RBT:
    def __init__(self):
        self.root = None

    def insert(self, val):
        a = rbtNode(val)
        if self.root == None:
            a.colour = rbtNode.BLACK
            self.root = a
        else:
            self.root.insert(a)

            a.fixTreeInsert(self.root)
    
    def delete(self, val):
        self.root = self.root.delete(val)
        #par.fixTreeDelete(self.root)
    
    def __repr__(self):
        return repr(self.root)
        





import heapq
import itertools

class PriorityQueue:
    REMOVED = "<removed-task>"
    def __init__(self):
        self.__counter = itertools.count()
        self.__map = {}
        self.__q = []

    def add(self, i, prio=0):
        if i in self.__map:
            self.__remove(i)
        count = next(self.__counter)
        entry = [prio, count, i]
        self.__map[i] = entry
        heapq.heappush(self.__q, entry)
    
    def __remove(self, task):
        entry = self.__map.pop(task)
        entry[-1] = PriorityQueue.REMOVED
    
    def pop(self):
        while self.__q:
            p, count, task = heapq.heappop(self.__q)
            if task != PriorityQueue.REMOVED:
                del self.__map[task]
                return task
        raise KeyError("Pop from empty queue")

