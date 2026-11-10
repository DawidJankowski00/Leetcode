from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def dfs(self, node):
        if not node:
            return []
        return self.dfs(node.left) + [node.val] + self.dfs(node.right)
    
    def __init__(self, root: Optional[TreeNode]):
        self.tab = self.dfs(root)
        self.curr = 0  

    def next(self) -> int:
        self.curr += 1
        return self.tab[self.curr-1]

    def hasNext(self) -> bool:
        return self.curr < len(self.tab)
