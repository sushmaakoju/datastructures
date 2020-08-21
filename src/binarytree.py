from .exception import Error, IndexOutOfBoundsException
from .utils import *
#Pseudocode
# For Binary Tree Inviariant: that has exactly two nodes.

class Node():
    def __init__(self, left, right, element):
        self.left = left
        self.right = right
        self.data = element

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def size(self):
        return self.size
    
    def height(self):
        return self.__height__(self.root)
    
    def __height__(self, node):
        if node == None:
            return 0
        return max(self.__height__(node.left), self.__height__(node.right)) + 1
    
    def insert_left(self, element):
        node = self.root
        if node == None:
            self.root = Node(None, None, element)
            self.size += 1
        else:
            if node.left == None:
                node.left = Node(None, None, element)
                self.size += 1
            else:
                tree = Node(None, None, element)
                tree.left = node.left
                self.root.left = tree
                self.size += 1

    def insert_right(self, element):
        node = self.root
        if node == None:
            self.root = Node(None, None, element)
            self.size += 1
        else:
            if node.right == None:
                node.right = Node(None, None, element)
                self.size += 1
            else:
                tree = Node(None, None, element)
                tree.right = node.right
                self.root.right = tree
                self.size += 1

    def __insert__(self, node, element):
        if node == None:
            self.root = Node(None, None, element)
            node = self.root
        else:
            if node.left == None:
                node.left = self.__insert__(node.left, element)
            elif node.right == None:
                node.right = self.__insert__(node.right, element)
            else:
                node = self.__insert__(node.left, element)
        return node


    def find(self, element):
        node = self.root
        return self.__find__(node, element)
    
    def __find__(self, node, element):
        if node == None:
            return False
        result = cmp(element, node.data)
        if result == 0:
            return True
        else:
            if node.left != None:
                return self.__find__(node.left, element)
            elif node.right != None:
                return self.__find__(node.right, element)
            else:
                if cmp(node.data, element) == 0:
                    return True
    
    def __iter__(self):
        if self.size == 0:
            return
        trav = self.root
        if trav != None:
            yield trav.data
            self.traverse_left(trav.left)
            self.traverse_right(trav.right)

    def traverse_left(self, node):
        if node.left != None:
            yield node.left.data
            return self.traverse_left(node.left)

    def traverse_right(self, node):
        if node.right != None:
            yield node.right.data
            return self.traverse_right(node.right)

    
            
