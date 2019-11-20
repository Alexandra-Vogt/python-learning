class bst:
    def __init__ (self, val):
        self.greater = None
        self.lesser  = None
        self.val     = val

    def insert(self, val):
        if val > self.val:
            self.greater = bst(val)
        else:
            self.lesser = bst(val)

    def getSmallest(self):
        if self.lesser:
            return self.lesser.getSmallest()
        else:
            return self.val

    def popSmallest(self):
        if self.lesser.lesser:
            self.lesser.popSmallest()
        else:
            self.lesser = None
            
            
def bstify(arr):
    bst = bst.arr[0]
    for val in arr:
        bst.insert(val)
    
    return bst
    
def debstify(bst):
    return list
    
def bstsort(list):
    deheapify(heapify(list))
    
