
#from __future__ import absolute_import, division, print_function
#__all__ = ['Error', 'IndexOutOfBoundsException']

class Error(Exception):
    '''
    This is Base Error class
    '''
    pass

class EmptyStackException(Exception):
    '''
    This is an Empty Stack exception
    '''
    def __init__(self, index, message="Stack is empty. Operation cannot be completed."):
        self.index = index
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.index} -> {self.message}'

class EmptyListException(Exception):
    '''
    This is an Empty List exception
    '''
    def __init__(self, index, message="List is empty. Operation cannot be completed."):
        self.index = index
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.index} -> {self.message}'

class IndexOutOfBoundsException(Exception):
    '''
    Raised when Index is out of bounds
    '''
    def __init__(self, index, message="Index is out of bounds."):
        self.index = index
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.index} -> {self.message}'
