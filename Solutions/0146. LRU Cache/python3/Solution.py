from collections import deque
from typing import List, Optional
from collections import OrderedDict

class ListNode:
    def __init__(self, x = 0, next = None):
        self.val = x
        self.next = next

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
    

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.data = {}

    def addNode(self, newNode):
        newNode.prev = self.head
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode
    
    def delNode(self, delNode):
        delNode.prev.next = delNode.next
        delNode.next.prev = delNode.prev

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        tmp = self.data[key]
        del self.data[key]
        self.delNode(tmp)
        self.addNode(tmp)
        self.data[key] = tmp
        return tmp.val

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            tmp = self.data[key]
            del self.data[key]
            self.delNode(tmp)
        
        if len(self.data) == self.cap:
            del self.data[self.tail.prev.key]
            self.delNode(self.tail.prev)
        self.addNode(Node(key, value))
        self.data[key] = self.head.next
