from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)] 
        for x, y in walls + guards:
            matrix[x][y] = 2
        directions = [(0,-1), (0,1), (-1,0), (1,0)]

        for gx, gy in guards:
            for dx,dy in directions:
                x = gx
                y = gy
                while True:
                    x += dx
                    y += dy
                    if x < 0 or y < 0 or x >= m or y >= n or matrix[x][y] == 2:
                        break
                    else:
                        matrix[x][y] = 1
        return sum(row.count(0) for row in matrix)

#0- clear cells
#1- guarded cells
#2- walls
#2- guards
