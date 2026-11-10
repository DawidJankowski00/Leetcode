from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        tmp = []

        def dfs(node):
            nonlocal tmp
            if node.left:
                dfs(node.left)
            tmp.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        n = len(tmp)
        if n == 1:
            return True
        for i in range(n-1):
            if tmp[i] >= tmp[i + 1]:
                return False
        return True
