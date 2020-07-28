import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

from collections import deque
from dynamicarray import DynamicArray 
from doublylinkedlist import DoublyLinkedList
from stack import Stack
from linked_queue import Queue
from treeset import TreeSet
from priority_queue import PriorityQueue
import time

#Create Dynamic Array and insert, delete elements
print("Dynamic array")
arr = DynamicArray()
arr.append("first")
arr.append("second")
arr.insert_at(1, "fourth")
arr.insert_at(0, "zeroeth")
arr.insert_at(2, "third")
arr.remove("second")
for i in range(0,len(arr)):
    print(arr.get(i))
arr.remove_at(2)
for i in range(0,len(arr)):
    print(arr.get(i))
arr.clear()
print(len(arr))

print("Doubly Linked List")

dl = DoublyLinkedList(1)
dl.add(2)
dl.add(3)
dl.add("fourth")
dl.add("fifth")
print(dl.to_string())
dl.add_first("first")
print(dl.to_string())
dl.add_last("last")
dl.remove_at(3)
print(dl.to_string())
dl.remove_first()
print(dl.to_string())


print("Stack")
stack =  Stack(1)
stack.push(2)
stack.push(3)
print(stack.to_string())
stack.pop()
print(stack.to_string())

print("Queue")
queue = Queue(4)
queue.offer(2)
print(queue.to_string())
queue.poll()
queue.offer(3)
print(queue.to_string())

print("TreeSort")
ts = TreeSet([3,7,7,1,3])
print(ts)
print(ts.get_right_least(4))
print(ts.get_left_greatest(4))
print(ts.get_left_greatest(3))
print(ts.get_right_least(3))
ts.add(4)
print(ts)
print(ts.get_right_least(4))
ts.add(0)
print(ts.get_left_greatest(4))

print("PriorityQueue")
nums = [3, 2, 5, 6, 7, 9, 4, 8, 1]
pq = PriorityQueue(size=len(nums), elements=None)
#elements =[3, 2, 5, 6, 7, 9, 4, 8, 1])
print(pq)
for n in nums: pq.add(n)
print(pq)
for i in range(0,): 
    print(pq.poll()==i)
print(pq.is_min_heap(0))
pq = None
pq = PriorityQueue(size=None, elements=nums)
print(pq)
print(pq.is_min_heap(0))
