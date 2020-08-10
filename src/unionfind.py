from .exception import Error

# All root nodes have root to self id[root] = root
#1) First find root of given component set (by default we have the component initialized to itself)
#2) Unify component sets i.e. two vertices that are connected by an edge.
# - This involves a) find roots of both elements and check if they are same 2) if they are not same,
#   replace root of element 1 with element 2's root which completes union operation.
#3) By default find, union, connected are O(N) (as we can see)
#4) After balance optimization i.e. using size to maintain weights of each component set, 
#5) O(log(N)) complexity for find, union and connected methods.
# - This involves 1) add sz[] and maintain weights of each set, by default sz of each component set is 1  
#   2) check if sz[root 1] < sz[root 2] , replace root of element 1 with element 2's root and viceversa
#   3) update the weights - add sz[root 1] to sz[ root 2]  
# summary - merge with set to the one that has larger 'weights' to 'balance' the trees
#6) Adding path compression in find, reduces complexity i.e.
#amortized complexity O(1) for find, union and connected.
# - This involves a) get root of the element 2) 'flatten' the path until traversed until the root
#   flattening - for a given p and its root, update id[p] to root and repeat until 
#   traversed all the way to root
#Note: complexity of union and connected is dependent on find, since both methods call find method.

class UnionFind:

    def __init__(self, size):
        self.size = size
        #size of components
        self.sz = [0]*size
        #id[i]=i is parent
        self.id = [0]*size
        #track number of components in unionfind
        self.num_components = size
        for i in range(0, size):
            self.id[i] = i
            self.sz[i] = 1
    
    #find which component set 'p' belongs to
    def find(self, p):
        """Find the root of given component set

        Args:
            p (): component set

        Returns:
            root: parent of component set
        """
        root = p
        #first find root of component set
        #search until parent of root is root itself
        #stop when 'p' is the root
        while root != self.id[root]:
            root = self.id[root]
        
        #now that you found root of 'p', compress the path
        #path compression (for amortized time complexity of )
        #now find method is O(1) instead of O(log(N)) or O(N)
        #make every node point to root
        while p !=  root:
            nxt = self.id[p]
            self.id[p] = root
            p = nxt
        return root
    
    #unify component sets containing 'p' and 'q'
    def unify(self, p,q ):
        #if already connected vertices, no need of unifying
        if self.connected(p,q):
            return
        #first find roots
        root1 = self.find(p)
        root2 = self.find(q)

        #add weights such that the component sets/tree is balanced during union operation
        #this makes sure smaller trees are connected to larger trees to avoid imbalanced trees
        #now union method is O(log(N)) instead of O(N), but with path compression,
        #union is also O(1)
        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1
        self.num_components -= 1
    
    def connected(self, p, q):
        """Return if p and q have same parent 

        Args:
            p : component set 1
            q : component set 2

        Returns:
            boolean: True if they belong to same parent
        """
        return self.find(p) == self.find(q)
    
    def component_size(self, p):
        return sz[self.find(p)] 
    
    def size(self):
        return self.size
    
    def components(self):
        return self.num_components

    
