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
from src.binarysearchtree import BinarySearchTree, TreeTraversalOrder
from src.hashtable import HashTable
from src.hashtable_chaining import ChainedHashTable
from src.fenwicktree import FenwickTree
from src.bitoperations import *
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
        dl = DoublyLinkedList(1, 0)
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
        for d in dl:
            print(d)

    def test_stack(self):
        print("Stack")
        stack =  Stack(1, 0)
        stack.push(2)
        stack.push(3)
        self.assertEqual(len(stack), 3)
        print(stack.to_string())
        stack.pop()
        self.assertEqual(len(stack), 2)
        print(stack.to_string())


    def test_queues(self):
        print("Queue")
        queue = Queue(4, 0)
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
        print("UnionFind")
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

 

    def test_binary_search_tree(self):
        print("BinarySearchTree")
        #test height
        bst = BinarySearchTree(None)
        self.assertEqual(bst.height(), 0)
        #test insert
        self.assertTrue(bst.insert("M"))
        self.assertEqual(bst.height(), 1)
        #layer 2
        bst.insert("J")
        self.assertEqual(bst.height(), 2)
        bst.insert("S")
        self.assertEqual(bst.height(), 2)

        #layer 3
        bst.insert("B")
        self.assertEqual(bst.height(), 3)
        bst.insert("N")
        self.assertEqual(bst.height(), 3)
        bst.insert("Z")
        self.assertEqual(bst.height(), 3)
    
        #layer 4
        bst.insert("A")
        self.assertEqual(bst.height(), 4)

        # test contains
        self.assertTrue(bst.contains("Z"))

        # test traversals
        bst.traverse(TreeTraversalOrder.INORDER)
        expected = ['A', 'B', 'J', 'M', 'N', 'S', 'Z']
        i = -1
        while bst.has_next():
            i += 1
            self.assertEqual(bst.next(), expected[i])
            
        bst.traverse(TreeTraversalOrder.PREORDER)
        expected = ['M', 'J', 'B', 'A', 'S', 'N', 'Z']
        i = -1
        while bst.has_next():
            i += 1
            self.assertEqual(bst.next(), expected[i])

        bst.traverse(TreeTraversalOrder.POSTORDER)
        expected = ['A', 'B', 'J', 'N', 'Z', 'S', 'M']
        i = -1
        while bst.has_next():
            i += 1
            self.assertEqual(bst.next(), expected[i])

        bst.traverse(TreeTraversalOrder.LEVELORDER)
        expected = ['A,', 'B,A', 'J,B', 'N,', 'Z,', 'S,NZ', 'M,JS']
        i = -1
        while bst.has_next():
            i += 1
            self.assertEqual(bst.next(), expected[i])

        bst = BinarySearchTree(None)
        bst.insert("A")
        self.assertEqual(bst.height(), 1)
        #test remove
        bst.insert("B")
        self.assertEqual(bst.size(), 2)
        self.assertTrue(bst.remove("B"))
        self.assertEqual(bst.height(), 1)
        self.assertEqual(bst.size(), 1)
        self.assertTrue(bst.remove("A"))
        self.assertEqual(bst.height(), 0)
        self.assertEqual(bst.size(), 0)

    def test_hashtable(self):
        print("HashTable")
        hashtable = HashTable(key=1,value=2,size=10)
        hashtable.add(2,2)
        self.assertTrue(hashtable.has_key(2))
        self.assertEqual(hashtable.get(2), 2)
    

    def test_chained_hashtable(self):
        print("ChainedHashTable")
        hashtable = ChainedHashTable(capacity=10)
        hashtable.add(1,2)
        hashtable.add(2,2)
        self.assertTrue(hashtable.has_key(2))
        self.assertEqual(hashtable.get(2), [2])
        hashtable.add(2,3)
        self.assertTrue(hashtable.has_key(2))
        self.assertEqual(hashtable.get(2), [2,3])
    

    def test_fenwick_tree(self):
        print("Fenwick Tree")
        ft = FenwickTree([1,2,2,4])
        self.assertEqual(ft.sum(1,4), 9)
        ft.point_update(3,1)
        self.assertEqual(ft.sum(1,4), 10)
        ft.set(4,0)
        self.assertEqual(ft.sum(1,4), 6)
        ft.get(2)
        ft = FenwickTree([-2,0,3,-5, 2, -1])
        self.assertEqual(ft.sum(1,3), 1)
        print(ft.tree)
        ft = FenwickTree([1,3,5])
        self.assertEqual(ft.sum(1,3), 9)
        print(ft.tree)
        ft.set(2,2)
        print(ft.tree)
        self.assertEqual(ft.sum(1,3), 8)
        

    
    def test_bitoperators(self):
        self.assertEqual(least_significan_bit(5), 1)