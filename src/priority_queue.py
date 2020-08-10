from .exception import EmptyListException
from .treeset import TreeSet
import math

class PriorityQueue():
    """Priority Queue using heap
    """
    def __init__(self, size=None, elements=None):
        if size != None:
            self.heapsize = size
            self.heapcapacity = 0
            self.heap = []*size
            self.map = dict()
        else:
            self.heapsize = self.heapcapacity = len(elements)
            self.heap = []* self.heapcapacity
            self.map = dict()
            for i in range(0, self.heapsize):
                self.map_add(elements[i], i)
                self.heap.append(elements[i])
            #heapify (heap invariant property since we use max heap to maintain priority)
            for i in range(max(0, (self.heapsize//2)-1),-1, -1 ):
                self.sink(i)
                
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return self.size() == 0
    
    def peek(self):
        if self.is_empty(): return None
        return self.heap[0]
    
    def clear(self):
        self.heap.clear()
        self.map.clear()
    
    def poll(self):
        if self.is_empty(): return None
        return self.remove_at(0)

    def add(self, element):
        self.heap.append(element)
        index_of_last_node = self.size() -1
        self.map_add(element, index_of_last_node)
        self.swim(index_of_last_node)

    def remove(self, element):
        if element == None: 
            return False
        index  = self.map_get(element)
        if index != None: 
            self.remove_at(index)
        return index != None
    
    def remove_at(self, i):
        index_of_last_node = self.size() -1
        removed_node = self.heap[i]
        self.swap(i, index_of_last_node)
        self.heap.remove(index_of_last_node)
        self.map_remove(removed_node, index_of_last_node)
        if i == index_of_last_node:
            return removed_node
        element = self.heap[i]
        self.sink(i)
        if self.heap[i] == element:
            self.swim(i)
        return removed_node
    
    def is_min_heap(self, i):
        """check heap invariant recursively starting from i

        Args:
            i: index to start (has to be 0 to start from root)

        Returns:
            bool: check if heap invariant is true
        """

        size = self.size()
        if i >= self.heapsize:
            return True
        left = 2*i+1
        right = 2*i+2
        if left < self.heapsize and self.less(i, left) == False:
            return False
        if right < self.heapsize and self.less(i, right) == False:
            return False       
        return self.is_min_heap(left) and self.is_min_heap(right)

    def sink(self, k):
        """dive into the tree till bottom level

        Args:
            k ([type]): [description]
        """
        heapsize = self.heapsize
        while True:
            left = 2*k+1
            right = 2*k+2
            smallest = left #assumig smallest is on left
            #check if right node is really 
            if right < heapsize and self.less(right, left):
                smallest = right
            if left >= heapsize or self.less(k, smallest):
                break
            #move to next level after "smallest" node
            self.swap(smallest, k)
            k= smallest
    
    def swim(self, k):
        """bottom up comparison tree

        Args:
            k : index to start from
        """
        parent = (k-1)//2
        while k >0 and self.less(k, parent):
            self.swap(parent, k)
            k = parent
            parent = (k-1)//2
    
    def swap(self, i, j):
        """swap the nodes i and j

        Args:
            i: node i
            j: node j
        """
        i_element = self.heap[i]
        j_element = self.heap[j]
        self.heap[i] = j_element
        self.heap[j] = i_element
        #now swap the map of value-indices
        self.map_swap(i_element, j_element, i, j)

    def less(self, i, j):
        """value of node i < = value of node j

        Args:
            i: node i
            j: node j

        Returns:
            boolean: True if value of node i <= value at node j
        """
        #print(i,j, len(self.heap))
        i_element = self.heap[i]
        j_element = self.heap[j]
        return i_element <= j_element

    def map_add(self, element, index):
        """add a node value and its index to map

        Args:
            element: value of node to b added
            index: index of element to be added
        """
        _treeset = self.map.get(element)
        if _treeset == None:
            tree_set = TreeSet()
            tree_set.add(index)
            self.map[element] = tree_set
        else:
            _treeset.add(index)

    def map_remove(self, element, index):
        _treeset = self.map.get(element)
        _treeset.remove(element)
        if len(_treeset) == 0:
            self.map.pop(element)
    
    def map_get(self, element):
        """Extract index position of a given value of node

        Args:
            element : value of a node
        """
        _tree_set = self.map.get(element)
        if _tree_set != None:
            return _tree_set.__getitem__(len(_tree_set) -1)
        return None

    def map_swap(self, i_element, j_element, i, j):
        """exchance index of two nodes

        Args:
            i_element ([type]): [description]
            j_element ([type]): [description]
            i ([type]): [description]
            j ([type]): [description]
        """
        set_i = self.map.get(i_element)
        set_j = self.map.get(j_element)

        set_i.remove(i)
        set_j.remove(j)

        set_i.add(j)
        set_j.add(i)

    def __str__(self):
        return str(self.heap)
