class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            result = grid[i][j]
            grid[i][j] = 0
            for i2, j2 in directions:
                result += dfs(i + i2, j + j2)
            return result


        result = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 0:
                    continue
                islandValue = dfs(i, j)
                if islandValue % k == 0:
                    result += 1
        return result