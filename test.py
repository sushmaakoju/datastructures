import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

from collections import deque
from src.dynamicarray import DynamicArray 
from src.doublylinkedlist import DoublyLinkedList
from src.stack import Stack
from src.linked_queue import Queue
from src.treeset import TreeSet
from src.priority_queue import PriorityQueue
from src.unionfind import UnionFind
import unittest

import time

class TestDataStructures(unittest.TestCase):

    def test_dynamic_array(self):
        print("Dynamic Array")
        #Create Dynamic Array and insert, delete elements
        arr = DynamicArray()
        arr.append("first")
        arr.append("second")
        arr.insert_at(1, "fourth")
        arr.insert_at(0, "zeroeth")
        arr.insert_at(2, "third")
        arr.remove("second")
        for i in range(0,len(arr)):
            print(arr.get(i))
        self.assertEqual(len(arr), 4)
        arr.remove_at(2)
        for i in range(0,len(arr)):
            print(arr.get(i))
        self.assertEqual(len(arr), 3)
        arr.clear()
        self.assertEqual(len(arr), 0)

    def test_doubly_linked(self):
        print("Doubly Linked List")
        dl = DoublyLinkedList(1)
        dl.add(2)
        dl.add(3)
        dl.add("fourth")
        dl.add("fifth")
        print(dl.to_string())
        self.assertEqual(len(dl), 4)
        dl.add_first("first")
        self.assertEqual(len(dl), 5)
        print(dl.to_string())
        dl.add_last("last")
        self.assertEqual(len(dl), 6)
        dl.remove_at(3)
        self.assertEqual(len(dl), 5)
        print(dl.to_string())
        dl.remove_first()
        self.assertEqual(len(dl), 4)
        print(dl.to_string())

    def test_stack(self):
        print("Stack")
        stack =  Stack(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(len(stack), 3)
        print(stack.to_string())
        stack.pop()
        self.assertEqual(len(stack), 2)
        print(stack.to_string())


    def test_queues(self):
        print("Queue")
        queue = Queue(4)
        queue.offer(2)
        self.assertEqual(len(queue), 2)
        print(queue.to_string())
        queue.poll()
        self.assertEqual(len(queue), 1)
        queue.offer(3)
        self.assertEqual(len(queue), 2)
        print(queue.to_string())


    def test_treeset(self):
        print("TreeSet")
        ts = TreeSet([3,7,7,1,3])
        self.assertEqual(len(ts), 5)
        print(ts)
        print(ts.get_right_least(4))
        print(ts.get_left_greatest(4))
        print(ts.get_left_greatest(3))
        print(ts.get_right_least(3))
        ts.add(4)
        self.assertEqual(len(ts), 6)
        print(ts)
        print(ts.get_right_least(4))
        ts.add(0)
        self.assertEqual(len(ts), 7)
        print(ts.get_left_greatest(4))


    def test_priotityqueue(self):
        print("PriorityQueue")
        nums = [3, 2, 5, 6, 7, 9, 4, 8, 1]
        pq = PriorityQueue(size=len(nums), elements=None)
        #elements =[3, 2, 5, 6, 7, 9, 4, 8, 1])
        print(pq)
        for n in nums: pq.add(n)
        self.assertEqual(pq.size(), len(nums))
        print(pq)
        for i in range(0,): 
            print(pq.poll()==i)
        print(pq.is_min_heap(0))
        pq = None
        pq = PriorityQueue(size=None, elements=nums)
        print(pq)
        print(pq.is_min_heap(0))
        self.assertEqual(pq.size(), len(nums))


    def test_unionfind(self):
        uf = UnionFind(5)
        self.assertEqual(uf.components(), 5)
        uf.unify(0,1)
        self.assertEqual(uf.components(), 4)
        uf.unify(1,0)
        self.assertEqual(uf.components(), 4)
        uf.unify(1,2)
        self.assertEqual(uf.components(), 3)
        uf.unify(0,2)
        self.assertEqual(uf.components(), 3)
        uf.unify(2,1)
        self.assertEqual(uf.components(), 3)
        uf.unify(3,4)
        self.assertEqual(uf.components(), 2)
        uf.unify(4,3)
        self.assertEqual(uf.components(), 2)
        uf.unify(1,3)
        self.assertEqual(uf.components(), 1)
        uf.unify(4,0)
        self.assertEqual(uf.components(), 1)

