import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]))
    print(time.time() - start)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(0, m//2):
            for j in range(0, n):
                matrix[j][i], matrix[j][m-1-i] = matrix[j][m-1-i], matrix[j][i]
        print(matrix)
        

if __name__ == '__main__':
    sys.exit(main())