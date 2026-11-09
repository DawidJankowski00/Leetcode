from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = None
        def dfs(node):
            nonlocal result
            if not node:
                return False
            d1 = dfs(node.left)
            d2 = dfs(node.right)
            tmp = ((node.val == q.val) or (node.val == p.val))
            if (d1 == True and d2 == True) or (d1 == True and tmp == True) or (d2 == True and tmp == True):
                result = node
                return False
            return d1 or d2 or tmp
        dfs(root)
        return result
