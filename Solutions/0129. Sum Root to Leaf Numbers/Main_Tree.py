from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.sumNumbers(create_tree_from_list([4,9,0,5,1])))
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, sum, line):
            result = 0
            sum = sum * line
            sum += node.val
            if not node.left and not node.right:
                result += sum
            else:
                if node.right:
                    result += dfs(node.right, sum, 10)
                if node.left:
                    result += dfs(node.left, sum, 10)
            return result
        return dfs(root, 0, 1)

if __name__ == '__main__':
    sys.exit(main())