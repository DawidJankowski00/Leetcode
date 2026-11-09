from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.lcaDeepestLeaves(create_tree_from_list([3,5,1,6,2,0,8,None,None,7,4])))
    print(time.time() - start)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree_from_list(data: List[Optional[int]]) -> Optional[TreeNode]:
    if not data:
        return None

    iter_data = iter(data)
    root = TreeNode(next(iter_data))
    queue = deque([root])

    while queue:
        node = queue.popleft()
        try:
            left_val = next(iter_data)
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)

            right_val = next(iter_data)
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)

        except StopIteration:
            break

    return root

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
        

if __name__ == '__main__':
    sys.exit(main())