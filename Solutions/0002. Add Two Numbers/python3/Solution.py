
import sys
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nodeToList(node):
    p1 = []
    tmp = node
    while (True):
        p1.append(tmp.val)
        if tmp.next == None:
            break
        else:
            tmp = tmp.next
    return p1

def listToNode(val):
    result = ListNode(val.pop())
    for i in range(0, len(val)):
        result = ListNode(val.pop(), result)
    return result

def main():
    l1 = listToNode([9,9,9,9,9,9,9])
    l2 = listToNode([9,9,9,9])
    sol = Solution()
    print(nodeToList(sol.addTwoNumbers(l1, l2)))

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        result = head
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            tmp = l1val + l2val + carry
            if tmp >=10:
                carry = 1
            else:
                carry = 0
            newNode = ListNode(tmp%10)
            result.next = newNode
            result = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next

if __name__ == '__main__':
    sys.exit(main())