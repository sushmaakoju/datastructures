
from .exception import EmptyListException, IndexOutOfBoundsException

# Pseudocode:
# All hash table operations cost O(1) time complexity
# for hash generation use Python's default hash method
# create a table (of type array) of a specified size or default size of 10
# Hash method: hash(key) % size (must be 'hash(key) mod length') 
# is deterministic. For making it uniform hash function, i.e.
# for hash collision, a) Separate chaining b) open address 
# c) double hashing d) linear probing - implemented in other hashtable variations.
# default, naive implementation(not handling hash collision):
# Implementation scheme of add(key, value): a) generate hash for the key
# b) case: table is empty, so simple add arr[hashedindex ] = [] and append to values list at hashedindex with value.
# c) case: table is not empty: a) index already exists in table so just overwrite like in dict in python 
# (handle this in hash collision technique later) b) index is not already in table, so just append. 
# Hash collision scheme is simple: overwrite the value if keyhash already exists. (since hash must deterministic)

class HashTable():
    """Simple case implementation of Hash table.
       There is an table with an index of hashed keys each with key,value pair.
       Operations supported: add, put, insert, get
    """
    def __init__(self,key=None, value=None, size=10):
        self.table = [None] * size
        self.size = size
        if key != None and value != None:
            self.add(key, value)
    
    def hash(self, key):
        """Hash the given key and normalize the hash value (to avoid negative hash values)

        Args:
            key (object) : key to insert and generate hash value for

        Returns:
            positive integer: hashed index 
        """
        size = len(self.table)
        return hash(key) % size
    
    def has_key(self, key):
        index = self.hash(key)
        return self.table[index] != None
    
    def clear(self):
        self.table = []
        self.size = 0
    
    def add(self, key, value):
        """Add a key, value pair to the Hash table.

        Args:
            key (object): key to be added
            value (object): corresponding value of the key
        """        
        self.insert(key, value)
    
    def put(self, key, value):
        """Put a key, value pair to the Hash table.

        Args:
            key (object): key to be added
            value (object): corresponding value of the key
        """
        self.insert(key, value)
    
    # Naive case (this add function does not handle hash collision)
    def insert(self, key, value):
        """Insert a key, value pair to the Hash table.

        Args:
            key (object): key to be added
            value (object): corresponding value of the key
        """
        index = self.hash(key)
        if self.table[index] != None:
            #overwrite like dict in python
            for k in self.table[index]:
                if k[0] == key:
                    k[1] = value
                    break
            #key not in current tableay, needs to be added
            else:
                self.table[index].append([key, value])
        #empty tableay
        else:
            self.table[index] = []
            self.table[index].append([key, value])
        
    def get(self, key):
        """Get the value of the key

        Args:
            key (object): key to look up

        Raises:
            KeyError: Exception raised if key does not exist.

        Returns:
            [type]: retrieved value of the key
        """
        index = self.hash(key)
        if self.table[index] == None:
            raise KeyError()
        else:
            for k in self.table[index]:
                if k[0] == key:
                    return k[1]
        raise KeyError()
