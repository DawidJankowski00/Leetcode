from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        mytable = {}
        for m in matrix:
            tmp = tuple(m)
            if tmp in mytable:
                mytable[tmp] += 1
            else:
                mytable[tmp] = 1
            tmp = tuple(x ^ 1 for x in m)
            if tmp in mytable:
                mytable[tmp] += 1
            else:
                mytable[tmp] = 1
        return max(mytable.values())
