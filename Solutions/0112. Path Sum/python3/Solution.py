from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr):
            curr += node.val
            result = False
            if node.left:
                if dfs(node.left, curr):
                    result = True
            if node.right:
                if dfs(node.right, curr):
                    result = True

            if not node.left and not node.right:
                if curr == targetSum:
                    return True
            return result

        if not root:
            return False

        return dfs(root, 0)
