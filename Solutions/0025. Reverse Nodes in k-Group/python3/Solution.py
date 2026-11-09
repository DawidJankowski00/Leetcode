from collections import deque
from typing import List, Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tmp = [0] * k
        curr = head
        st = head
        test = False
        while curr != None:
            for i in range(k):
                tmp[i] = curr.val
                curr = curr.next
                if curr == None and i < k-1:
                    test = True
                    break
            if test:
                break
            for i in range(1, k+1):
                st.val = tmp[-i]
                st = st.next
        return head
