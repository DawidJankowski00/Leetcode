from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        qu = [root]
        result = [root.val]
        while qu:
            lvl = []
            for node in qu:
                if node:
                    lvl.append(node.left)
                    lvl.append(node.right)
            qu = lvl
            arr = [node.val for node in lvl if node]
            if arr:
                result.append(max(arr))
        return result
