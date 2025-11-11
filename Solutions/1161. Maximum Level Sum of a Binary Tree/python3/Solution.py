from collections import defaultdict, deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = - float('inf')

        queue = deque([root])
        result = 0
        curr = 1
        while queue:
            n = len(queue)
            tmp = 0
            for _ in range(n):
                node = queue.popleft()
                tmp += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if tmp > max_sum:
                max_sum = tmp
                result = curr
            curr += 1
        return result
