from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.isSameTree(create_tree_from_list([1,None,1]),create_tree_from_list([1,None,1])))
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q == None and p == None:
            return True
        if q == None or p == None:
            return False
        def dfs(p, q):
            if p.val != q.val:
                return False
            if p.left != None and q.left != None:
                if p.right != None and q.right != None:
                    return dfs(p.left,q.left) and dfs(p.right,q.right)
                return p.right == None and q.right == None and dfs(p.left, q.left)
            if p.right != None and q.right != None:
                return  p.left == None and q.left == None and dfs(p.right,q.right)
            return p.right == None and q.right == None and p.left == None and q.left == None
        return dfs(p,q)

        

if __name__ == '__main__':
    sys.exit(main())