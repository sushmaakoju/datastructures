from .exception import Error
import bisect
# use bisect to sort to right
# add ceiling and floor 
# ceiling using bisect_right to return least elem that is >= element being looked up
# floor using bisect_left to return greatest elem that is <= element being looked up
# insert by using insort which bisect_right
class TreeSet():
    """Binary Tree Set
       Does allow duplicate elements (required for PriorityQueues, Binary heaps etc)
       Tree set is automatically sorted everytime a new element is added.
    """
    def __init__(self, elements=[]):
        self.treeset = []
        self.add_all(elements)
    
    def add_all(self, elements):
        for element in elements:
            self.add(element)
    
    def add(self, element):
        """Add a new element and sort

        Args:
            element: element to be added to sorted tree set
        """
        if element != None:
            bisect.insort(self.treeset, element)
    
    def get_right_least(self, element):
        """get least element from right tree such that
        all elements > = the given 'element'

        Args:
            element : element 

        Returns:
            ceiling element: least element from elements >= given element
        """
        #get that index of least element from right tree 
        index = bisect.bisect_right(self.treeset, element)
        if self[index - 1] == element:
            return element
        return self.treeset[bisect.bisect_right(self.treeset, element)]
    
    def get_left_greatest(self, element):
        """get greatest element from left tree such that
        all elements < = the given 'element'

        Application: to insert an element

        Args:
            element : element 

        Returns:
            floor element: greatest element from elements <= given element
        """
        #get that index of greatest element from left tree 
        index = bisect.bisect_left(self.treeset, element)
        if self[index] == element:
            return element
        return self.treeset[bisect.bisect_left(self.treeset, element)-1]
    
    def pop(self, element):
        self.treeset.pop(element)

    def remove(self, element):
        try:
            self.treeset.remove(element)
        except ValueError:
            return False
        return True

    def clear(self):
        self.treeset = []
    
    def clone(self):
        return TreeSet(self.treeset)
    
    #just return generator
    def __iter__(self):
        for element in self.treeset:
            yield element

    def __eq__(self, value):
        if isinstance(value, TreeSet):
            return self.treeset == target.treeset
        elif isinstance(value, list):   
            return self.treeset == value
    
    def __getitem__(self, num):
        return self.treeset[num]
    
    def __str__(self):
        return str(self.treeset)
    
    def __len__(self):
        return len(self.treeset)
    

    
