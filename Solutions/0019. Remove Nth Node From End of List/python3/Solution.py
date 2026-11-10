from collections import deque
from typing import List, Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
