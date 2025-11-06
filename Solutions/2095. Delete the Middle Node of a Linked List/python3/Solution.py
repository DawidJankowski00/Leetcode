from typing import Optional
class ListNode:
    def __init__(self, x = 0, next = None):
        self.val = x
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        n = head
        midle = ListNode(0, head)
        while n.next:
            n = n.next
            midle = midle.next
            if n.next:
                n = n.next
        midle.next = midle.next.next
        return head
