from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        def dLeft(node):
            d = 0
            while node:
                node = node.left
                d += 1
            return d
        
        def dRight(node):
            d = 0
            while node:
                node = node.right
                d += 1
            return d
        
        l = dLeft(root)
        r = dRight(root)

        if l == r:
            return 2**(l+1) - 1
        return self.countNodes(root.left) + 1 + self.countNodes(root.right)
