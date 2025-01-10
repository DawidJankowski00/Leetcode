from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.reverseBetween(create_list_from_list())
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

if __name__ == '__main__':
    sys.exit(main())