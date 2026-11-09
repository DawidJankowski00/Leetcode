import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
    print(time.time() - start)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        results = []

        m, n = len(heights), len(heights[0])
        a = set()
        p = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(x, y, visited):
            visited.add((x,y))
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) not in visited:
                        if heights[nx][ny] >= heights[x][y]:
                            dfs(nx, ny, visited)

        for i in range(m):
            dfs(i, 0, p)
            dfs(i, n-1, a)
        for i in range(n):
            dfs(0, i, p)
            dfs(m-1, i, a)

        for v in a:
            if v in p:
                results.append(v)
        return results
        

if __name__ == '__main__':
    sys.exit(main())