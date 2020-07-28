from doublylinkedlist import DoublyLinkedList
from exception import EmptyListException

class Queue(DoublyLinkedList):

    def __init__(self, element):
        super().__init__(element)
        self.offer(element)

    #o(1)
    def poll(self):
        """removes last node from stack

        Raises:
            EmptyStackException: raised if stack is empty

        Returns:
            data: data of node that was removed
        """
        if self.is_empty():
            raise EmptyListException( "Queue is empty. Operation cannot be completed")
        return self.remove_first()
    
    #o(1)
    def offer(self, element):
        """offer the node to queued list

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
    
    def peek(self):
        """Peek first

        Raises:
            EmptyStackException: raised if stack is empty

        Returns:
            data: returns data of node
        """
        if self.is_empty():
            raise EmptyListException( "Queue is empty. Operation cannot be completed")
        return self.peek_first()
    