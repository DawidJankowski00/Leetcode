from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.*****(create_list_from_list())
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
        

if __name__ == '__main__':
    sys.exit(main())