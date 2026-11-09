import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    
    print(sol.maxMatrixSum([[0,0,0],[0,0,0],[0,0,0]]))
    print(time.time() - start)

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        result = minus = 0
        lowest = 10**5
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < 0:
                    result -= matrix[i][j]
                    minus += 1
                    if lowest > -matrix[i][j]:
                        lowest = -matrix[i][j]
                else:
                    result += matrix[i][j]
                    if lowest > matrix[i][j]:
                        lowest = matrix[i][j]
        if minus % 2 == 0:
            return result
        else:
            return result - lowest *2

if __name__ == '__main__':
    sys.exit(main())