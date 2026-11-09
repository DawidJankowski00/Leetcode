from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        min_diff = float('inf')
        prev = -float('inf')
        def traverse(node):
            nonlocal min_diff, prev
            if not node:
                return
            traverse(node.left)
            min_diff = min(min_diff, node.val - prev)
            prev = node.val
            traverse(node.right)
        traverse(root)
        return min_diff
