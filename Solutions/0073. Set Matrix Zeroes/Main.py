import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
    print(time.time() - start)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        row = False
        col = False
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i == 0:
                        row = True
                    if j == 0:
                        col = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,n):
            if matrix[i][0] == 0:
                for j in range(m):
                    matrix[i][j] = 0
        for i in range(1,m):
            if matrix[0][i] == 0:
                for j in range(n):
                    matrix[j][i] = 0
        if col:
            for i in range(n):
                matrix[i][0] = 0
        if row:
            for i in range(m):
                matrix[0][i] = 0
        

if __name__ == '__main__':
    sys.exit(main())