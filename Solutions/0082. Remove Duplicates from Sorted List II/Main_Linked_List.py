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

if __name__ == '__main__':
    sys.exit(main())