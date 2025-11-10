from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_value):
            if not node:
                return 0
            tmp = 0
            if node.val >= max_value:
                tmp += 1
                max_value = node.val
            return tmp + dfs(node.left, max_value) + dfs(node.right, max_value)
        return dfs(root, -100000)
