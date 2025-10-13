from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.countNodes(create_tree_from_list([1,2,3,4,5,6])))
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
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        def dLeft(node):
            d = 0
            while node:
                node = node.left
                d += 1
            return d
        
        def dRight(node):
            d = 0
            while node:
                node = node.right
                d += 1
            return d
        
        l = dLeft(root)
        r = dRight(root)

        if l == r:
            return 2**(l+1) - 1
        return self.countNodes(root.left) + 1 + self.countNodes(root.right)


if __name__ == '__main__':
    sys.exit(main())