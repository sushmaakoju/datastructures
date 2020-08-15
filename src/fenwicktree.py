from .exception import *
from .bitoperations import *
from copy import deepcopy
# Finding range sum [i,j] in a flat array 
class FenwickTree():
    """Fenwick Tree is Binary Indexed tree. 
    """
    def __init__(self, values):
        self.size = len(values)
        self.values = values
        self.tree = [0]
        self.tree.extend(deepcopy(values))
        #one-based array
        for i in range(1,self.size):
            parent = i + least_significan_bit(i)
            if parent <= self.size:
                self.tree[parent] += self.tree[i]
    
    def prefix_sum(self, i):
        sum = 0
        while i > 0 :
            sum += self.tree[i]
            i &= ~least_significan_bit(i)
        print(sum)
        return sum
    
    def sum(self, i, j):
        if j < i:
            raise ValueError("Make sure j >= i")
        return self.prefix_sum(j) - self.prefix_sum(i-1)

    def point_update(self, i, x):
        while i <= self.size:
            self.tree[i] = self.tree[i] + x
            i += least_significan_bit(i)
        return self.tree
    
    def get(self, i):
        return self.sum(i,i)
    
    def set(self, i, val):
        return self.point_update(i , (val - self.sum(i,i)))