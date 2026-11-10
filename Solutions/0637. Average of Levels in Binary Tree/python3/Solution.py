from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sum = []
        queue = deque([root])
        while queue:
            curr = 0
            num_of_elements = len(queue)
            for _ in range(num_of_elements):
                node = queue.popleft()
                curr += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            sum.append(curr / num_of_elements)
        return sum
