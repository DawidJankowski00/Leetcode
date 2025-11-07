from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node, arr):
            if not node:
                return
            if not node.right and not node.left:
                arr.append(node.val)
            dfs(node.left, arr)
            dfs(node.right, arr)
        left = []
        right = []
        dfs(root1, left)
        dfs(root2, right)
        return left == right