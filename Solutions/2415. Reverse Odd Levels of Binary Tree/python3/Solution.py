from collections import deque
import sys
import time
from typing import List, Optional
def main():
    sol = Solution()
    start = time.time()
    print(sol.reverseOddLevels([2,3,5,8,13,21,34]))
    print(time.time() - start)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def DFS(nodel, noder, level):
            if not nodel or not noder:
                return
            if level % 2 == 0:
                nodel.val, noder.val = noder.val, nodel.val
            DFS(nodel.left, noder.right, level + 1)
            DFS(nodel.right, noder.left, level + 1)
        
        DFS(root.left, root.right, 0)
        return root
        

if __name__ == '__main__':
    sys.exit(main())