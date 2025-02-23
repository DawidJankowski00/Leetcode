from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.constructFromPrePost([1,2,4,5,3,6,7],[4,5,2,6,7,3,1]))
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
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def helper(pre, post):
            if not pre:
                return None
            if len(pre) == 1:
                return TreeNode(post.pop())
            node = TreeNode(post.pop())
            ind = pre.index(post[-1])
            node.right=helper(pre[ind:],post)
            node.left=helper(pre[1:ind],post)
            return node
            
        return helper(preorder, postorder)
        

if __name__ == '__main__':
    sys.exit(main())