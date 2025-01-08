from collections import deque
import sys
import time
from typing import List, Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
def main():
    sol = Solution()
    start = time.time()
    print(sol.mergeTwoLists(create_list_from_list([1,2,4]),create_list_from_list([1,3,4])))
    print(time.time() - start)

if __name__ == '__main__':
    sys.exit(main())

