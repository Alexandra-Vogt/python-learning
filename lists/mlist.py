class node:
    def __init__(self, val):
        self.nextNode = None
        self.prevNode = None
        self.val      = val
        

class mlist:
    def __init__(self):
        self.headNode = None
        self.tailNode = None
        self.size     = 0

    def getNode(self, index):
        currentNode = self.headNode
        i = 0
        while i < index:
            currentNode = currentNode.nextNode
            i += 1
        return currentNode.val
        
    def deleteNode(self, index):
        prevNode = None
        currentNode = self.headNode
        i = 0
        while i < index:
            prevNode = currentNode
            currentNode = currentNode.nextNode
            i += 1
        if prevNode and index == self.size - 1:
            prevNode.nextNode = None
            self.tailNode = prevNode
        elif prevNode:
            prevNode.nextNode = None
        else:
            self.headNode = None
            self.tailNode = None
        self.size -= 1

    def pushBack(self, val):
        if self.size > 0:
            self.tailNode.nextNode = node(val)
            self.tailNode.nextNode.prevNode = self.tailNode
            self.tailNode = self.tailNode.nextNode
        else:
            self.headNode = node(val)
            self.tailNode = self.headNode
        self.size += 1
            
    def popBack(self):
        if self.tailNode.prevNode:
            self.tailNode = self.tailNode.prevNode
            self.tailNode.nextNode = None
        else:
            self.tailNode = None
            self.headNode = None
        self.size -= 1


        
