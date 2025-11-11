from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        result = 0
        #True = last Left
        #False = last Right

        def dfs(node, curr, direction):
            nonlocal result
            if not node:
                if curr > result:
                    result = curr
                return
            if direction == None:
                dfs(node.left, 0, True)
                dfs(node.right, 0, False)
            elif direction == True:
                dfs(node.left, 0, True)
                dfs(node.right, curr+1, False)
            elif direction == False:
                dfs(node.left, curr+1, True)
                dfs(node.right, 0, False)
            


        dfs(root, 0, None)
        return result

        