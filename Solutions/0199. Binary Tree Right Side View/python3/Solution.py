from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = {}
        def bfs(node, h):
            if not node:
                return
            nonlocal result
            result[h] = node.val
            bfs(node.left, h+1)
            bfs(node.right, h+1)
        bfs(root, 0)
        tmp = []
        for v in result.keys():
            tmp.append(result[v])
        return tmp
