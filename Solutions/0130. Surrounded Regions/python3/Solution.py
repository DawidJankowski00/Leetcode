from collections import deque
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n):
                return
            if board[x][y] == "O":
                board[x][y] = "0"
                for tx, ty in directions:
                    dfs(x + tx, y + ty)
            

        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n-1] == "O":
                dfs(i, n-1)

        for i in range(n):
            if board[0][i] == "O":
                dfs(0, i)
            if board[m-1][i] == "O":
                dfs(m-1, i)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "0":
                    board[i][j] = "O"
                
        