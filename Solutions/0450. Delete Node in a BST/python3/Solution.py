from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            elif root.left:
                root.val = self.find_left(root.left)
                root.left = self.deleteNode(root.left, root.val)
            else:
                root.val = self.find_right(root.right)
                root.right = self.deleteNode(root.right, root.val)
        return root
    
    def find_left(self, root: TreeNode):
        while root.right:
            root = root.right
        return root.val

    def find_right(self, root: TreeNode):
        while root.left:
            root = root.left
        return root.val


        
        
