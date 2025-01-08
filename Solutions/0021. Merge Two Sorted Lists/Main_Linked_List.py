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
        result = None
        tmp = []
        while True:
            if list1 == None:
                if list2 == None:
                    break
                tmp.append(list2.val)
                list2 = list2.next
            elif list2 == None:
                if list1 == None:
                    break
                tmp.append(list1.val)
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    tmp.append(list1.val)
                    list1 = list1.next
                else:
                    tmp.append(list2.val)
                    list2 = list2.next
        tmp.reverse()
        for v in tmp:
            result = ListNode(v, result)
        return result
        
def main():
    sol = Solution()
    start = time.time()
    print(sol.mergeTwoLists(create_list_from_list([1,2,4]),create_list_from_list([1,3,4])))
    print(time.time() - start)

if __name__ == '__main__':
    sys.exit(main())

