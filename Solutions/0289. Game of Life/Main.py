import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
    print(time.time() - start)

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        n = len(board)
        m = len(board[0])
        directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        for i in range(n):
            for j in range(m):
                tmp = 0
                for x,y in directions:
                    if 0 <= i+x < n and 0 <= j+y < m:
                        if board[i+x][j+y] == 1 or board[i+x][j+y] == 3:
                            tmp += 1
                if board[i][j] == 0:
                    if tmp == 3:
                        board[i][j] = 2
                if board[i][j] == 1:
                    if tmp == 2 or tmp == 3:
                        continue
                    else:
                        board[i][j] = 3
        for i in range(n):
            for j in range(m):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0
        
        

if __name__ == '__main__':
    sys.exit(main())