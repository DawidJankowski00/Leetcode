from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.maxPathSum(create_tree_from_list([1,2,3])))
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -1001

        def dfs(node):
            nonlocal result
            if not node:
                return 0
            tmp1 = dfs(node.left) 
            tmp2 = dfs(node.right)

            result = max(result, node.val + tmp1 + tmp2)
            if tmp1 + node.val > 0 or tmp2 + node.val > 0:
                return max(tmp1, tmp2) + node.val
            else:
                return 0
        dfs(root)

        return result 

if __name__ == '__main__':
    sys.exit(main())