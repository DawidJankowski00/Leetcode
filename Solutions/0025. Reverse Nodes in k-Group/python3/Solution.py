from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.reverseKGroup(create_list_from_list([1,2,3,4,5]),2))
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
        

if __name__ == '__main__':
    sys.exit(main())