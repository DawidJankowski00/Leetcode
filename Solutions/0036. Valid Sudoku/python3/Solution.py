from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        box = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in rows[i]: return False
                    else: rows[i][board[i][j]] = 1
                    if board[i][j] in cols[j]: return False
                    else: cols[j][board[i][j]] = 1

                    k = (i // 3 ) * 3 + j // 3
                    if board[i][j] in box[k]: return False
                    else: box[k][board[i][j]] = 1
        return True
