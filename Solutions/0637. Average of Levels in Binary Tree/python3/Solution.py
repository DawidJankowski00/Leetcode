from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.averageOfLevels(create_tree_from_list([3,9,20,None,None,15,7])))
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sum = []
        queue = deque([root])
        while queue:
            curr = 0
            num_of_elements = len(queue)
            for _ in range(num_of_elements):
                node = queue.popleft()
                curr += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            sum.append(curr / num_of_elements)
        return sum
        

if __name__ == '__main__':
    sys.exit(main())