from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = 0

        def dfs(node):
            nonlocal curr
            t = None
            if node.left:
                t = dfs(node.left)
                if t is not None:
                    return t
            curr += 1
            if curr == k:
                return node.val
            if node.right:
                t = dfs(node.right)
                if t is not None:
                    return t
            return t
        
        return dfs(root)
