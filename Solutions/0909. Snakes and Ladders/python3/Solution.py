from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        tp = {} 

        for i in range(n):
            for j in range(n):
                row_from_bottom = n - 1 - i
                
                if row_from_bottom % 2 == 0:
                    current_square = row_from_bottom * n + (j + 1)
                else:
                    current_square = row_from_bottom * n + (n - j)

                if board[i][j] != -1:
                    tp[current_square] = board[i][j]
                else:
                    tp[current_square] = current_square

        end = n * n
        queue = deque()
        queue.append((1, 0)) 
        
        visited = {1}

        while queue:
            q, s = queue.popleft() 
            
            if q == end:
                return s
            
            for i in range(1, 7):
                next_square_candidate = q + i
                
                if next_square_candidate <= end:
                    target_square = tp[next_square_candidate]
                    
                    if target_square not in visited:
                        visited.add(target_square)
                        queue.append((target_square, s + 1))
                        
        return -1