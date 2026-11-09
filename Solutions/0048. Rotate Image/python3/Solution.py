from typing import List

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
