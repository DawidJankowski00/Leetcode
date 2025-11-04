from collections import Counter, defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        matrix_dict = Counter(zip(*grid))
        n = len(grid)
        result = 0
        for i in range(n):
            result += matrix_dict.get(tuple(grid[i]), 0)
        return result
        
