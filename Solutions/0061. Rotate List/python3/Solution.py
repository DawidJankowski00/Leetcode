from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.rotateRight(create_list_from_list([1,2,3,4,5]), 2))
    print(time.time() - start)

class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head == None:
            return head

        last = head
        n = 1
        while last.next:
            last = last.next
            n += 1
        last.next = head
        tmp = head
        for _ in range(n - (k % n) - 1):
            tmp = tmp.next

        ans = tmp.next
        tmp.next = None
        return ans

if __name__ == '__main__':
    sys.exit(main())