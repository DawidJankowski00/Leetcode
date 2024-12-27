import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
    print(time.time() - start)

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
        

if __name__ == '__main__':
    sys.exit(main())