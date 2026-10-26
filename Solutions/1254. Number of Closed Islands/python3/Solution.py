class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 1:
                return
            grid[i][j] = 1
            for i2, j2 in directions:
                dfs(i + i2, j + j2)

        for i in range(m):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][n-1] == 0:
                dfs(i, n-1)

        for j in range(n):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[m-1][j] == 0:
                dfs(m-1, j)

        result = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    result += 1
                    dfs(i, j)
                

        return result
