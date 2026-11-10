from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def helper(pre, post):
            if not pre:
                return None
            if len(pre) == 1:
                return TreeNode(post.pop())
            node = TreeNode(post.pop())
            ind = pre.index(post[-1])
            node.right=helper(pre[ind:],post)
            node.left=helper(pre[1:ind],post)
            return node
            
        return helper(preorder, postorder)
