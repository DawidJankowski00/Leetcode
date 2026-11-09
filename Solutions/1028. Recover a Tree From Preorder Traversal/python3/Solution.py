from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
