from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        cols = [0] * n
        rows = [0] * m
        cordscol = [0] * (m*n+1)
        cordsrow = [0] * (m*n+1)
        for i in range(n):
            for j in range(m):
                cordscol[mat[i][j]] = i
                cordsrow[mat[i][j]] = j
        
        for i, v in enumerate(arr):
            c, r = cordscol[v], cordsrow[v]
            cols[c] += 1
            if cols[c] >= m:
                return i
            rows[r] += 1
            if rows[r] >= n:
                return i
