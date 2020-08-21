#!/bin/python3

import math
import os
import random
import re
import sys
from .hashtable_chaining import ChainedHashTable, Key

class Set:
    def __init__(self):
        self.size = 0
        self.myset = ChainedHashTable(10, 0.75)

    def get(self, index):
        if index <0 or index >= self.size:
            raise Exception("Index out of bounds")
        return self.myset.get(index)

    def put(self, val):
        if not self.__contains__(val):
            self.myset.put(val, val)
            self.size += 1
            return 1
        return -1

    #o(n)
    def remove(self, val):
        i = 0
        if Key(val) in self.myset.keys():
            self.myset.remove(val)
            self.size -= 1
            return True

    def __contains__(self, val):
        return self.myset.has_key(val)
    
    def __len__(self):
        return self.size
