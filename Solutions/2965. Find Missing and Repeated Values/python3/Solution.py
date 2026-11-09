from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        tab = {}
        result = []
        for i in grid:
            for j in i:
                if j in tab:
                    result.append(j)
                tab[j] = True
        for i in range(1, n*n + 1):
            if i in tab:
                continue
            else:
                result.append(i)
                break
        return result
