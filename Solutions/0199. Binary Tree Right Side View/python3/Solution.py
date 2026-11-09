from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.rightSideView(create_tree_from_list([1,2,3,None,5,None,4])))
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = {}
        def bfs(node, h):
            if not node:
                return
            nonlocal result
            result[h] = node.val
            bfs(node.left, h+1)
            bfs(node.right, h+1)
        bfs(root, 0)
        tmp = []
        for v in result.keys():
            tmp.append(result[v])
        return tmp
        

if __name__ == '__main__':
    sys.exit(main())