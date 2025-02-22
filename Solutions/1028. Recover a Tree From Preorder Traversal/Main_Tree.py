from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.recoverFromPreorder("1-2--3--4-5--6--7"))
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
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        curr = 0
        root = TreeNode()
        for i in range(0, len(traversal)):
            if traversal[i] == '-':
                curr += 1
            else:
                k = i
                while len(traversal) > k and traversal[k] != '-':
                    k += 1
                root.val = int(traversal[i:k])
                break

        tmp = 0
        j = 0
        l_start = 0
        r_start = 0
        for i in range(0, len(traversal)):
            if traversal[i] == '-':
                tmp += 1
            else:
                if tmp == curr + 1:
                    if l_start == 0:
                        l_start = j
                    else:
                        r_start = j
                        break
                tmp = 0
                j = i+1
        if l_start != 0:
            if r_start == 0:
                root.left = self.recoverFromPreorder(traversal[l_start:])
            else:
                root.left = self.recoverFromPreorder(traversal[l_start:r_start])
                root.right = self.recoverFromPreorder(traversal[r_start:])
        return root
        

if __name__ == '__main__':
    sys.exit(main())