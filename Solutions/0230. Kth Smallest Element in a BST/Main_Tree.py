from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.kthSmallest(create_tree_from_list([3,1,4,None,2]),1))
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = 0

        def dfs(node):
            nonlocal curr
            t = None
            if node.left:
                t = dfs(node.left)
                if t is not None:
                    return t
            curr += 1
            if curr == k:
                return node.val
            if node.right:
                t = dfs(node.right)
                if t is not None:
                    return t
            return t
        
        return dfs(root)

        

if __name__ == '__main__':
    sys.exit(main())