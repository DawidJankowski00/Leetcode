from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.partition(create_list_from_list([1,4,3,2,5,2]), 3))
    print(time.time() - start)

class ListNode:
    def __init__(self, x = 0, next = None):
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        tmp = head
        l = ListNode(-1)
        lt = l
        r = ListNode(-1)
        rt = r

        while tmp:
            if tmp.val >= x:
                rt.next = ListNode(tmp.val)
                rt = rt.next
            else:
                lt.next = ListNode(tmp.val)
                lt = lt.next
            tmp = tmp.next
        lt.next = r.next


        return l.next
        

if __name__ == '__main__':
    sys.exit(main())