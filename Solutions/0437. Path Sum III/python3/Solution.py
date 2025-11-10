from collections import defaultdict
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr):
            nonlocal acc
            if not node:
                return
            curr += node.val
            ct = acc[curr - targetSum]
            acc[curr] += 1
            ct += dfs(node.left, curr) + dfs(node.right, curr)
            acc[curr] -= 1
            return ct

        acc = defaultdict(int)
        acc[0] = 1
        return dfs(root, 0)