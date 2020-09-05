from .utils import cmp

class Node():
    def __init__(self, left, right, element : object):
        self.left = left
        self.right = right
        self.data = element
        self.bf = 0
        self.height = 0

    def get_height(self):
        return self.height
    
    def get_balancingfactor(self):
        return self.bf
    
    def get_right(self):
        return self.right
    
    def get_left(self):
        return self.left

class AVLTree():
    def __init__(self, node : Node):
        self.root = node
        self.node_count = 0
    
    def size(self):
        return self.node_count

    def is_empty(self):
        return (self.size() == 0)

    
    def contains(self, element):
        """check if element already exists in the AVL tree. This is the public method.

        Args:
            element (comparable): element

        Returns:
            boolean: True if element alreayd exists
        """
        result = self.__contains__(self.root, element) 
        return result
    
    def __contains__(self, node : Node, element):
        """This is the private method to recursively find the element from left/right tree.
           Returns True if AVL contains the element else False.

        Args:
            node (Node): node to lookup if element exists in AVL
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
        #if element == node.data, element exists in AVL
        else:
            return True
    
    def insert(self, element):
        """insert element to AVL. This is the public method to insert an element.

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

    def __insert__(self, node : Node, element):
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
        #for AVL -> add balancing factor and height for the node ()
        self.update(node)
        #lastly return after balancing - height >= ceil(log₂(n+1)-1)
        return self.balance(node)

    def update(self, node : Node):
        left_node_height = node.left.height if node.left != None else -1
        right_node_height = node.right.height if node.right != None else -1
        node.height = 1 + max(left_node_height, right_node_height)

        node.bf = right_node_height - left_node_height
    
    def balance(self, node):
        #left-heavy subtree
        if node.bf == -2:
            if node.left.bf <= 0 :
                return self.leftleftcase(node)
            else:
                return self.leftrightcase(node)
        elif node.bf == +2:
            if node.right.bf >= 0:
                return self.rightrightcase(node)
            else:
                return self.rightleftcase(node)
        return node
    
    def leftleftcase(self, node : Node):
        return self.right_rotation(node)
    
    def leftrightcase(self, node : Node):
        node.left = self.left_rotation(node.left)
        return self.leftleftcase(node)
    
    def rightrightcase(self, node : Node):
        return self.left_rotation(node)
    
    def rightleftcase(self, node : Node):
        node.right = self.right_rotation(node.right)
        return self.rightrightcase(node)
    
    def left_rotation(self, node : Node):
        new_parent = node.right
        node.right = new_parent.left
        new_parent.left = node
        self.update(node)
        self.update(new_parent)
        return new_parent
    
    def right_rotation(self, node : Node):
        new_parent = node.left
        node.left = new_parent.right
        new_parent.right = node
        self.update(node)
        self.update(new_parent)
        return new_parent


    def find_min(self, node : Node):
        """Find left most node (which has the smallest value)

        Args:
            node (Node): node to look up for left most node

        Returns:
            Node: the left most node
        """
        while node.left != None:
            node = node.left
        return node
    
    def find_max(self, node : Node):       
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
        """Remove element from AVL. This is the public method.

        Args:
            element (comparable): element to be removed from AVL

        Returns:
            boolean : True if element exists in AVL and has been removed successfully 
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

    def __remove__(self, node : Node, element):
        """This is the private method to remove element from the AVL.
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
        self.update(node)
        return self.balance(node)
    
    def validate_bst_invariant(self, node : Node):
        if node == None:
            return True

        val = node.data
        is_valid = True
        if node.left != None:
            is_valid = is_valid and cmp(node.left.data, val) < 0
        if node.right != None:
            is_valid = is_valid and cmp(node.right.data, val) > 0
        return (is_valid and self.validate_bst_invariant(node.left) and 
                self.validate_bst_invariant(node.right))