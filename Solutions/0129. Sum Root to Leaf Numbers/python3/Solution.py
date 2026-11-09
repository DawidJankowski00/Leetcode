from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, sum, line):
            result = 0
            sum = sum * line
            sum += node.val
            if not node.left and not node.right:
                result += sum
            else:
                if node.right:
                    result += dfs(node.right, sum, 10)
                if node.left:
                    result += dfs(node.left, sum, 10)
            return result
        return dfs(root, 0, 1)
