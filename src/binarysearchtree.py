from .stack import Stack
from .linked_queue import Queue
from enum import Enum
from .utils import *
#Pseudocode:
#Binary Search Tree: is a binary tree with Binary Search Invariant 
#such that left tree elements are smaller and right tree elements are larger.
#1) BST node: Node has left, right nodes and element. 
#Leaf nodes have "None" type subtree nodes with valid data.
#2) insertion : insert element to left of root if element < rootnode.data else to right
#3) removal : cases:  a) node to remove is a leaf node b) node to remove has right subtree and no left subtree
#   c) node to remove has left subtree and no right subtree d) node to remove has both left and right subtrees
#   for case a) is straightforward : just remove leaf node and update parent's reference to leaf node.
#   for case b) and c) - simply swap with immediate child node i.e. child of right subtree for case b) and
#   child of left subtree for case c)
#   for case d) happens to be slightly complex: node to be removed has left and right subtrees.
#   we find successor by following i) find left most node in right subtree and swap the data of node to be rmeoved with 
#   that-left-most-node-from-right-subtree. node.right = root node of right subtree after removal.
#   we can also use find_max to handle case d) i.e. find rightmost node in left subtree. 
# Tree traversal : 1) preorder (print node.data before traversing to subtrees) 2) inorder (print during the traversal) and postorder (print data after traversal).
# use queues/stacks to pop and push traversed nodes/root nodes
# avg case: O(log(n)) and worst case O(n)
class Node():
    def __init__(self, left, right, element):
        self.left = left
        self.right = right
        self.data = element
class TreeTraversalOrder(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3
    LEVELORDER = 4
    
class BinarySearchTree():
    """Binary Search Tree: is a binary tree with Binary Search Invariant 
       such that left tree elements are smaller and right tree elements are larger.
    """
    def __init__(self, element):
        self.root = None
        self.node_count = 0
        if element != None:
            self.insert(element)
        self.stack = Stack(None, 0)
        self.index = -1
        self.sorted = []
    
    def size(self):
        return self.node_count
    
    def insert(self, element):
        """insert element to BST. This is the public method to insert an element.

        Args:
            element (comparable): element to be inserted

        Returns:
            boolean : True if inserted successfully. False if element already exists
        """
        if self.contains(element):
            return False
        else:
            self.root = self.__insert__(self.root, element)
            self.node_count += 1
            return True

    def __insert__(self, node, element):
        """Inserts an element in the Binary Search tree

        Args:
            node : the root node to insert into
            element (comparable): element to be inserted

        Returns:
            node: the updated root node
        """
        if node == None:
            self.root = Node(None, None, element)
            node = self.root
        else:
            if cmp(element, node.data) < 0:
                node.left = self.__insert__(node.left, element)
            else:
                node.right = self.__insert__(node.right, element)
        return node
    
    def contains(self, element):
        """check if element already exists in the BST. This is the public method.

        Args:
            element (comparable): element

        Returns:
            boolean: True if element alreayd exists
        """
        result = self.__contains__(self.root, element) 
        return result
    
    def __contains__(self, node, element):
        """This is the private method to recursively find the element from left/right tree.
           Returns True if BST contains the element else False.

        Args:
            node (Node): node to lookup if element exists in BST
            element (comparable): element to lookup

        Returns:
            boolean: True of element exists in Binary search tree
        """
        if node == None:
            return False
        
        result = cmp(element, node.data)

        #search in left tree if element < node.data
        if result < 0:
            return self.__contains__(node.left, element)
        #else search in right tree if element > node.data
        elif result > 0:
            return self.__contains__(node.right, element)
        #if element == node.data, element exists in BST
        else:
            return True
    
    def find_min(self, node):
        """Find left most node (which has the smallest value)

        Args:
            node (Node): node to look up for left most node

        Returns:
            Node: the left most node
        """
        while node.left != None:
            node = node.left
        return node
    
    def find_max(self, node):       
        """Find right most node (which has the largest value)

        Args:
            node (Node): node to look up for right most node from

        Returns:
            Node : the rightmost node
        """
        while node.right != None:
            node = node.right
        return node
    
    def remove(self, element):
        """Remove element from BST. This is the public method.

        Args:
            element (comparable): element to be removed from BST

        Returns:
            boolean : True if element exists in BST and has been removed successfully 
            or else returns False.
        """
        print(self.contains(element))
        if self.contains(element):
            print("contains")
            self.root = self.__remove__(self.root, element)
            self.node_count -= 1
            return True
        else:
            return False

    def __remove__(self, node, element):
        """This is the private method to remove element from the BST.
            for 4 standard cases of element removal: a) element is a leaf node
            b) element has only left subtree c) element has only right subtree
            d) element has both right and left subtrees
        Args:
            node (Node): node to look up
            element (comparable): element to be removed

        Returns:
            node : the updated node after removal of the element
        """
        if node == None:
            return False
        
        result = cmp(element, node.data)

        #search in left tree if element < node.data
        if result < 0:
            node.left = self.__remove__(node.left, element)
        #search in right tree if element > node.data
        elif result > 0:
            node.right = self.__remove__(node.right, element)
        #found the node we want to remove
        else:
            #case where there is only right subtree or no subtree at all.
            #just swap the node with element with right node.
            if node.left == None:
                return node.right
            #case
            elif node.right == None:
                return node.left
            else:
                tmp = self.find_min(node.right)
                node.data = tmp.data
                # we go to right subtree and remove that-leftmost-node-from-rightsubtree 
                # that we found i.e. tmp.data. So we maintain only single node with that
                # that-leftmost-node-from-rightsubtree we found. We do this,
                # since we are manually swapping the data of the nodes and updating
                # reference to removed node's right subtree as well without duplicate nodes.
                node.right = self.__remove__(node.right, tmp.data)
        return node
    
    def preorder_traversal(self, node):
        """Traverse through Binary search tree using stack and preorder

        Args:
            node (Node): node to traverse

        Returns:
            comparable: data of node traversed
        """
        if node == None:
            return
        expected_count = self.node_count
        self.sorted.append(node.data)
        if node.left != None:
            self.preorder_traversal(node.left)
        if node.right != None:
            self.preorder_traversal(node.right)
    
    def inorder_traversal(self, node):
        """Traverse through Binary search tree using stack and inorder

        Args:
            node (Node): node to traverse

        Returns:
            comparable: data of node traversed
        """
        if node == None:
            return
        expected_count = self.node_count
        if node.left != None:
            self.inorder_traversal(node.left)
        self.sorted.append(node.data)
        if node.right != None:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        """Traverse through Binary search tree using stack and postorder

        Args:
            node (Node): node to traverse

        Returns:
            comparable: data of node traversed
        """
        if node == None:
            return
        expected_count = self.node_count
        if node.left != None:
            self.postorder_traversal(node.left)
        if node.right != None:
            self.postorder_traversal(node.right)
        self.sorted.append(node.data)

    def levelorder_traversal(self, node):
        """Level order traversal of the Binary search tree. Uses Breadth first search approach.

        Args:
            node (Node): node to traverse

        Returns:
            comparable: data of node
        """
        level_list = ''
        level_list += str(node.data) + ','
        if node.left != None:
            level_list += str(node.left.data)
            self.levelorder_traversal(node.left)
        if node.right != None:
            level_list += str(node.right.data)
            self.levelorder_traversal(node.right)
        if not level_list == '':
            self.sorted.append(level_list)
        return node.data
    
    def traverse(self, tree_traversal_order=TreeTraversalOrder.INORDER):
        """Traverse by Tree Traversal Order (preorder, postorder, inorder, level order)

        Args:
            tree_traversal_order ( TreeTraversalOrder, optional): Tree Traversal Order 
            Defaults to TreeTraversalOrder.INORDER.
            Select from TreeTraversalOrder.PREORDER,TreeTraversalOrder.POSTORDER,
            TreeTraversalOrder.LEVELORDER, TreeTraversalOrder.INORDER.
        """
        #reset
        self.sorted = []
        self.index = -1

        #and traverses
        if tree_traversal_order == TreeTraversalOrder.INORDER:
            return self.inorder_traversal(self.root)
        elif tree_traversal_order == TreeTraversalOrder.PREORDER:
            return self.preorder_traversal(self.root)
        elif tree_traversal_order == TreeTraversalOrder.POSTORDER:
            return self.postorder_traversal(self.root)
        elif tree_traversal_order == TreeTraversalOrder.LEVELORDER:
            return self.levelorder_traversal(self.root)
        else:
            return None
            

    def height(self):
        """This is a public method to get the height of the Binary search tree.

        Returns:
            __height__(node): calls private method to get height of subtrees
        """
        return self.__height__(self.root)
    
    def __height__(self, node):
        if node == None:
            return 0
        return max(self.__height__(node.left), self.__height__(node.right)) + 1
    
    def has_next(self):
        return (self.index +1) < len(self.sorted)
    
    #return smallest from stack
    def next(self):
        self.index += 1
        return self.sorted[self.index]




