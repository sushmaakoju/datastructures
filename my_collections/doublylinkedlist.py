#from __future__ import absolute_import, division, print_function
from exception import IndexOutOfBoundsException

#Consists of nodes.
# 1) define node with previous, next and data parameters
# 2) initialize doubly linked list with a head and tail nodes and then size =0
# by default add at last -> set tail.next to new node and new node.prev = tail
# 3) add at first -> set head.prev = new node and newnode.next = head and newnode.prev = None
# 4) remove last -> set tail.prev.next = None and tail = None
# 5) remove at first -> set head.next.prev = None, head.next = None and head =None
# 6) add at index -> traverse till node at index-1, store temp = node at index-1
# and add new node with prev = temp and next = temp.next, then temp.next.prev = newnode, temp.next = newnode
# 7) remove at index -> traverse till index-1 (if index < size/2) then traverse from head else from tail
# 8) remove node -> node.next.prev = node.prev and node.prev.next = node.next
# 9) clear, peek first and peek last, index of, to string (regular implementations)
#__all__=['DoublyLinkedList']
class Node():
    """Node class with data, previous and next node references.
    """
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
    
    def __str__(self):
            return str(self.data)

class DoublyLinkedList():
    '''
    This is a Doubly linked list
    '''
    
    def __init__(self, data):
        """Initialize this node with data
        """
        self.size = 0
        self.head = Node(data, None, None)
        self.tail = Node(data, None, None)
    
    def clear(self):
        """Clear all nodes from linked list
        """
        trav = self.head
        while trav != None:
            next = trav.next
            trav.prev = trav.next = None
            trav.data = None
            trav = next
        self.head = self.tail = trav = None
        self.size = 0
    
    def size(self):
        """Return size of linked list

        Returns:
            size: returns size of linked list
        """
        return self.size
    
    def is_empty(self):
        """Returns True if list is empty

        Returns:
            bool: returns true if list is empty
        """
        return self.size == 0
    
    def add(self, element):
        """Add an element to Double linked list. Adds at end of list.

        Args:
            element ([type]): Data element to be added to new node.
        """
        self.add_last(element)
    
    def add_last(self, element):
        """Adds new node at end of the list

        Args:
            element ([type]): Data element to be added to new node.
        """
        if self.is_empty():
            self.head = self.tail = Node(element, None, None)
        else:
            self.tail.next = Node(element, self.tail, None)
            self.tail = self.tail.next
        self.size += 1
    
    def add_first(self, element):
        """Adds new node at begining of the list

        Args:
            element (type): Data element to be added to new node.
        """
        if self.is_empty():
            self.head = self.tail = Node(element, None, None )
        else:
            self.head.prev = Node(element, None, self.head)
            self.head = self.head.prev
        self.size += 1
    
    #o(n)
    def add_at(self, index, element):
        """Adds new node at specific index of list

        Args:
            index (type): Index to add the node in the list.
            element (type): Data element to be added to new node.
        """
        if index < 0 or index > self.size:
            raise IndexOutOfBoundsException(index, 'Index is out of bounds.')
        if index == 0:
            self.add_first(element)
            return
        if index == self.size:
            self.add_last(element)
            return
        
        temp = self.head
        for i in range(0, index-1):
            temp = temp.next
        newNode = Node(element, temp, temp.next)
        temp.next.prev = newNode
        temp.next = newNode
        self.size += 1
    
    def peek_first(self):
        """Peeks to the head node

        Raises:
            RuntimeError: Check if list is empty

        Returns:
            data: Returns data of the first node
        """
        if self.is_empty():
            raise RuntimeError('Empty list')
        return self.head.data
    
    def peek_last(self):
        """Peeks to the tail node

        Raises:
            RuntimeError: Check if list is empty

        Returns:
            data: Returns data of the first node
        """
        if self.is_empty():
            raise RuntimeError('Empty list')
        return self.tail.data
    
    #o(1)
    def remove_first(self):
        """Remove first node

        Raises:
            RuntimeError: Check if list is empty

        Returns:
            data: data of the removed node
        """
        if self.is_empty():
            raise RuntimeError('Empty list')
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        else:
            self.head.prev = None

        return data

    #o(1)
    def remove_last(self):
        """Remove last node

        Raises:
            RuntimeError: Check if list is empty

        Returns:
            data: data of the removed node
        """
        if self.is_empty():
            raise RuntimeError('Empty list')
        data = self.tail.data
        tail = self.tail.prev
        self.tail.prev.next = None
        self.tail = tail

        self.size -= 1
        return data

    #o(1)
    def remove(self, node):
        """Remove a node

        Args:
            node (Node): Node to be removed

        Returns:
            data: Data of the removed node
        """
        if node.prev == None:
            self.remove_first()
        if node.next == None:
            self.remove_last()
        
        node.next.prev = node.prev
        node.prev.next = node.next
        data = node.data

        node.prev = node.next = node = None
        self.size -= 1
        return data

    #o(1)
    def remove_at(self, index):
        """Remove node at specified index

        Args:
            index (int): index of node to be removed

        Raises:
            IndexOutOfBoundsException: if index is out of bounds

        Returns:
            data: data of the node that was removed
        """
        if index < 0 or index > self.size:
            raise IndexOutOfBoundsException(index, 'Index is out of bounds.')
        if index == 0:
            self.remove_first()
            return
        if index == self.size:
            self.remove_last()
            return
        
        if index < self.size/2 :
            i = 0
            trav = self.head
            while i!= index:
                trav = trav.next
                i += 1
                if i == index-1:
                    break
        else:
            i= self.size -1
            trav  = self.tail
            while i!= index:
                trav = trav.prev
                i -= 1
                if i == index-1:
                    break 
        return self.remove(trav)

    #o(n)
    def index_of(self, obj):
        """Gte index of data

        Args:
            obj : the data paramter of the node

        Returns:
            index: index of the data of the node in the list
        """
        index = 0
        trav = self.head
        while trav != None:
            if obj == trav.data :
                return index
            else:
                index +=1
        return -1

    def to_string(self):
        """Return datas of all nodes in string format

        Returns:
            string: the concatenated data of all node
        """
        trav = self.head
        data_str = ""
        while trav != None :
            data_str += trav.__str__()
            if trav.next != None:
                data_str += ","
            trav = trav.next
        return data_str
