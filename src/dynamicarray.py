#from __future__ import absolute_import, division, print_function

print('__file__={0:<35} | __name__={1:<25} | __package__={2:<25}'.format(__file__,__name__,str(__package__)))
from .exception import IndexOutOfBoundsException

import ctypes

#__all__=['DynamicArray']
#This is an implementation of Dynamic Array.
#Pseudo code;
# 1) set length =0 and capacity = 0 (where capacity is actual array length before/after add/remove)
# 2) set an empty array of type T (we do not know yet which "type" the array elements are)
# 3) we can use static array to store all elements of dynamic array before increasing the size
# dynamic array, for add/remove methods.
# 4) define set, get, append, size, clear methods for dynamic array
# uses ctypes (for arrays)

class DynamicArray(object):
    '''
    This is a Dynamic Array class (~List in Python)
    '''
    def __init__(self):
        self.len = 0
        self.capacity = 1
        self.arr = self.create_array(self.capacity)
    
    def create_array(self, capacity):
        """Return new array with new capacity

        Args:
            capacity (integer): new size of array

        Returns:
            array: an array with size
        """
        return (capacity * ctypes.py_object)()
    

    def __len__(self):
        """Get current size of the Dynamic array

        Returns:
            length: current size of array]
        """
        return self.len
    
    def is_empty(self):
        if self.len == 0:
            return arr

    # O(1) constant time
    def get(self, index):
        """Get index of the element in the Dynamic array

        Args:
            index ([type]): index of element to look up for
        
        Returns:
            element: return element
        """
        if index < 0 or index >= self.len:
            raise IndexOutOfBoundsException(index, "Index is out of bounds.")
            return
        return self.arr[index]

    #o(n)
    def indexof(self, element):
        """Get index of the element in the Dynamic array

        Args:
            element ([type]): [element to look up index for]
        """
        for i in range(self.len):
            if element == None:
                if self.arr[i] == None:
                    return i
            else:
                if element == self.arr[i]:
                    return i
        return -1
    
    def contains(self, element):
        """Check if element exists in the array

        Args:
            element (type): Element to look up

        Returns:
            [type]: returns true if element exists
        """
        return self.indexof(element) != -1

    def __str__(self):
        string_values = ""
        for i in range(self.len):
            string_values += self.arr[i]
        return string_values

    # O(1) constant time
    def set(self, index, element):
        """Set an element at specified index

        Args:
            index (type): index of element to set
            element (type): element to replace

        Raises:
            IndexOutOfBoundsException: If index is >= length of array or < 0, 
        """
        if index < 0 or index >= self.len:
            raise IndexOutOfBoundsException(index, "Index is out of bounds.")
            return

        self.arr[index] = element

    #append  -> n iterations -> o(n)
    def append(self, element):
        """Adds element at end of the array

        Args:
            item (type): element to insert
        """        
        #need to increase the capacity of the array
        self.capacity *= 2
        temp = self.create_array(self.capacity)

        for i in range(self.len):
            temp[i] = self.arr[i]
        self.arr = temp
        self.arr[self.len] = element
        self.len += 1
    
    #o(n)
    def insert_at(self, index, element):
        """Adds element at specified index

        Args:
            item (type): element to insert
        """        
        if index < 0 or index >= self.len:
            raise IndexOutOfBoundsException(index, "Index is out of bounds. Insertion is not possible")
            return
        #need to increase the capacity of the array
        self.capacity *= 2

        temp = self.create_array(self.capacity)
        for i in range(self.len-1, index-1, -1):
            temp[i+1] = self.arr[i]
        temp[index] = element
        for i in range(0, index):
            temp[i] = self.arr[i]
        self.arr = temp
        self.len += 1
    
    #o(n)
    def remove_at(self, index):
        """Removes an element from specific index

        Args:
            index (index): index of array
        """
        if self.len == 0:
            print("Array is empty. Deletion is not possible.")
            return
        
        if index < 0 or index >= self.len:
            raise IndexOutOfBoundsException(index, "Index is out of bounds. Deletion is not possible")
            return

        temp = self.create_array(self.len-1)
        j = 0
        for i in range(self.len):
            if i == index:
                j -= 1
            else:
                temp[j] = self.arr[i]
            j += 1
        self.arr = temp
        self.capacity = self.len - 1
        self.len -= 1
    
    def remove(self, element):
        """Remove element if exists in the array

        Args:
            element (type): Element to be removed
        
        Returns:
            [type]: returns true if element exists
        """
        index = self.indexof(element)
        if index == -1:
            return False
        self.remove_at(index)
        return True
    
    def clear(self):
        """Clear all elements from the array
        """
        self.arr = self.create_array(1)
        self.len = 0

        