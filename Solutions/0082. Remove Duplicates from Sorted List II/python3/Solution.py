from collections import deque
from typing import List, Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        tmp = None
        all = [0 for _ in range(200)]
        
        while head != None:
            all[head.val + 100] += 1
            head = head.next
        
        tr = True
        for i in range(200):
            if all[i] == 1:
                if tr:
                    result = ListNode(i-100)
                    tmp = result
                    tr = False
                else:
                    tmp.next = ListNode(i - 100)
                    tmp = tmp.next

        return result
