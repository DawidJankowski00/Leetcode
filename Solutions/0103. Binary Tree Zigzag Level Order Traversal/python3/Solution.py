from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        operator = True
        while queue:
            l = len(queue)
            tmp = []
            for _ in range(l):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if operator:
                result.append(tmp)
                operator = False
            else:
                tmp.reverse()
                result.append(tmp)
                operator = True
        return result
