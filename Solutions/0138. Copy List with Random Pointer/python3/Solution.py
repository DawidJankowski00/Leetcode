import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.*****())
    print(time.time() - start)

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        cop = {}
        while curr != None:
            new_node = Node(curr.val)
            cop[curr] = new_node
            curr = curr.next
        curr = head
        while curr != None:
            cop[curr].next = cop.get(curr.next)
            cop[curr].random = cop.get(curr.random)
            curr = curr.next
        return cop[head]

if __name__ == '__main__':
    sys.exit(main())