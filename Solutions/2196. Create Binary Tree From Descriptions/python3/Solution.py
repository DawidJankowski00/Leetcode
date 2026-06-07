from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        Root = set()
        Register = {}
        for parent, child, isLeft in descriptions:
            if parent not in Register:
                Root.add(parent)
                Register[parent] = TreeNode(parent)
            if child not in Register:
                Register[child] = TreeNode(child)
            if isLeft:
                Register[parent].left = Register[child]
            else:
                Register[parent].right = Register[child]
            Root.discard(child)
        return Register[Root.pop()]
            