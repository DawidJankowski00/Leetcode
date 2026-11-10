from collections import deque
from typing import List, Optional

class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

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
