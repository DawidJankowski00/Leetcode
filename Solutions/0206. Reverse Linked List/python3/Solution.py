from typing import Optional
class ListNode:
    def __init__(self, x = 0, next = None):
        self.val = x
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        curr = head
        next_item = head.next
        while next_item:
            curr.next = prev
            prev = curr
            curr = next_item
            next_item = next_item.next
        curr.next = prev
        return curr