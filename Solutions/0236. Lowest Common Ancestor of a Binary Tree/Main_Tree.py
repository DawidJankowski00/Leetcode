from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.lowestCommonAncestor(create_tree_from_list([3,5,1,6,2,0,8,None,None,7,4]),5,1))
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = None
        def dfs(node):
            nonlocal result
            if not node:
                return False
            d1 = dfs(node.left)
            d2 = dfs(node.right)
            tmp = ((node.val == q.val) or (node.val == p.val))
            if (d1 == True and d2 == True) or (d1 == True and tmp == True) or (d2 == True and tmp == True):
                result = node
                return False
            return d1 or d2 or tmp
        dfs(root)
        return result

        

if __name__ == '__main__':
    sys.exit(main())