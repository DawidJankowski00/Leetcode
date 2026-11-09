from collections import deque
from typing import List, Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        st = None
        tmp = []
        for i in range(1, left):
            curr = curr.next
        st = curr
        for i in range(right-left+1):
            tmp.append(curr.val)
            curr = curr.next
        for i in range(1, right-left + 2):
            st.val = tmp[-i]
            st = st.next
        return head
