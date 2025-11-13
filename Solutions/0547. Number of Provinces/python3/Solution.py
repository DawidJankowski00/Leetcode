from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        to_visit = set()
        result = 0
        n = len(isConnected)
        for i in range(n):
            if i in visited:
                continue
            visited.add(i)
            result += 1
            to_visit.add(i)
            while len(to_visit) > 0:
                k = to_visit.pop()
                visited.add(k)
                for j in range(n):
                    if isConnected[k][j] == 1:
                        if j not in visited and j not in to_visit:
                            to_visit.add(j)
        return result