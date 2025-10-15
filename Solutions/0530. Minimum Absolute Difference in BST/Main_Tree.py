from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.getMinimumDifference(create_tree_from_list([4,2,6,1,3])))
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
    def getMinimumDifference(self, root: TreeNode) -> int:
        min_diff = float('inf')
        prev = -float('inf')
        def traverse(node):
            nonlocal min_diff, prev
            if not node:
                return
            traverse(node.left)
            min_diff = min(min_diff, node.val - prev)
            prev = node.val
            traverse(node.right)
        traverse(root)
        return min_diff
        

if __name__ == '__main__':
    sys.exit(main())