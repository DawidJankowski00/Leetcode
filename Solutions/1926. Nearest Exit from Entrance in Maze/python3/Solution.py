from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        maze_n = len(maze)
        maze_m = len(maze[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        queue = deque()
        
        start_x, start_y = entrance[0], entrance[1]
        queue.append((start_x, start_y))
        visited.add((start_x, start_y))
        
        result = 0

        while queue:
            n = len(queue)
            result += 1

            for _ in range(n):
                x, y = queue.popleft()
                
                for xd, yd in directions:
                    nx = xd + x
                    ny = yd + y

                    is_in_bounds = nx >= 0 and ny >= 0 and nx < maze_n and ny < maze_m
                    
                    if is_in_bounds and maze[nx][ny] != "+":
                        
                        is_on_border = (nx == 0 or ny == 0 or nx == maze_n - 1 or ny == maze_m - 1)
                        
                        if is_on_border and (nx != start_x or ny != start_y):
                            return result
                            
                        if (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
                            
        return -1
