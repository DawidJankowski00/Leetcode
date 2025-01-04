import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    print(time.time() - start)

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        result = 1
        points.sort(key=lambda x: x[1])
        stop = points[0][1]
        for v in points[1:]:
            if v[0] > stop:
                stop = v[1]
                result += 1
        return result

        

if __name__ == '__main__':
    sys.exit(main())