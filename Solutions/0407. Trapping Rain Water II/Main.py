import sys
import time
from typing import List
import heapq
def main():
    sol = Solution()
    start = time.time()
    print(sol.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
    print(time.time() - start)

class Solution:
    def trapRainWater(self, height_map: List[List[int]]) -> int:
        rows = len(height_map)
        cols = len(height_map[0])
        if rows < 3 or cols < 3:
            return 0

        water_trapped = 0
        min_heap = []

        for r in range(rows):
            for c in [0, cols - 1]:
                heapq.heappush(min_heap, (height_map[r][c], r, c))
                height_map[r][c] = -1

        for c in range(cols):
            for r in [0, rows - 1]:
                heapq.heappush(min_heap, (height_map[r][c], r, c))
                height_map[r][c] = -1

        max_level = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while min_heap:
            height, x, y = heapq.heappop(min_heap)
            max_level = max(max_level, height)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and height_map[nx][ny] != -1:
                    if height_map[nx][ny] < max_level:
                        water_trapped += max_level - height_map[nx][ny]

                    heapq.heappush(min_heap, (height_map[nx][ny], nx, ny))
                    height_map[nx][ny] = -1

        return water_trapped
        

if __name__ == '__main__':
    sys.exit(main())