from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node, d):
            if node == None:
                return (None, d)
            a = helper(node.left, d+1)
            b = helper(node.right, d+1)
            
            if a[1] > b[1]:
                return a
            if a[1] < b[1]:
                return b
            return (node, a[1])
            
        return helper(root, 0)[0]
