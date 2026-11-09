from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        def dfs(node, d):
            if node == None:
                return d
            if node.right == None:
                if node.left == None:
                    return d
                return dfs(node.left, d+1)
            return max(dfs(node.left, d+1), dfs(node.right, d+1))
        return dfs(root, 1)
