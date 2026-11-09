from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.minimumOperations(create_tree_from_list([1,4,3,7,6,8,5,None,None,None,None,9,None,10])))
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
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        qu = [root]
        result = 0
        while qu:
            lvl = []
            for node in qu:
                if node:
                    lvl.append(node.left)
                    lvl.append(node.right)
            qu = lvl
            arr = [node.val for node in lvl if node]
            tmp = [(v, i) for i, v in enumerate(arr)]
            sorted_tmp = [i for _, i in sorted(tmp)]
            for i in range(len(sorted_tmp)):
                while i != sorted_tmp[i]:
                    j = sorted_tmp[i]
                    sorted_tmp[i], sorted_tmp[j] = sorted_tmp[j], sorted_tmp[i]
                    result += 1
        return result


if __name__ == '__main__':
    sys.exit(main())