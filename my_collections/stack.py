from doublylinkedlist import DoublyLinkedList
from exception import EmptyStackException

class Stack(DoublyLinkedList):

    #o(1)
    def pop(self):
        """removes last node from stack

        Raises:
            EmptyStackException: raised if stack is empty

        Returns:
            data: data of node that was removed
        """
        if self.is_empty():
            raise EmptyStackException()
        return self.remove_last()
    
    #o(1)
    def push(self, element):
        """push the node to stacked list

        Args:
            element: data of node to be added
        """
        self.add_last(element)
    
    def is_empty(self):
        """check if stack is empty

        Raises:
            EmptyStackException: raised if stack is empty

        Returns:
            bool: true or false
        """
        return self.size == 0
    
    #o(1)
    def peek(self):
        """[summary]

        Raises:
            EmptyStackException: raised if stack is empty

        Returns:
            data: returns data of node
        """
        if self.is_empty():
            raise EmptyStackException()
        return self.peek_first()
    