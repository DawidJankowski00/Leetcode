from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.deleteDuplicates(create_list_from_list([1,2,3,3,4,4,5])))
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        return dummy.next

if __name__ == '__main__':
    sys.exit(main())