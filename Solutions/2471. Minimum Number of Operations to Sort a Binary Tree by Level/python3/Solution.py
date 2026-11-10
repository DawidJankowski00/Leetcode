from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
