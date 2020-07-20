class Error(Exception):
    '''
    This is Base Error class
    '''
    pass

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
