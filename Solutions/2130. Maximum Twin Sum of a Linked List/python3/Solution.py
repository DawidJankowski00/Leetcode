from typing import Optional
class ListNode:
    def __init__(self, x = 0, next = None):
        self.val = x
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        nextnode = None
        prev = None
        while slow:
            nextnode = slow.next
            slow.next = prev
            prev = slow
            slow = nextnode
        
        result = 0

        while prev:
            curr = head.val + prev.val
            if curr > result:
                result = curr
            head = head.next
            prev = prev.next

        return result