from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.removeNthFromEnd(create_list_from_list([1,2,3,4,5]),2))
    print(time.time() - start)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_list_from_list(values):
    if not values:
        return None  

    head = ListNode(values[0])  
    current = head
    for value in values[1:]:
        current.next = ListNode(value)  
        current = current.next  
    return head

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = 0
        curr = head
        while curr != None:
            c += 1
            curr = curr.next
        if c == n:
            return head.next
        curr = head
        for _ in range(c-n-1):
            curr = curr.next
        curr.next = curr.next.next

        return head

if __name__ == '__main__':
    sys.exit(main())