from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -1001

        def dfs(node):
            nonlocal result
            if not node:
                return 0
            tmp1 = dfs(node.left) 
            tmp2 = dfs(node.right)

            result = max(result, node.val + tmp1 + tmp2)
            if tmp1 + node.val > 0 or tmp2 + node.val > 0:
                return max(tmp1, tmp2) + node.val
            else:
                return 0
        dfs(root)

        return result
