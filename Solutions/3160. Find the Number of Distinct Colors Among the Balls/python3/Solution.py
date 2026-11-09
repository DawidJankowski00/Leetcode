from collections import defaultdict
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.queryResults(4,[[1,4],[2,5],[1,3],[3,4]]))
    print(time.time() - start)

from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        color_count = {}
        curr = 0
        result = []

        for ball, color in queries:
            if ball in balls:
                prev_color = balls[ball]
                color_count[prev_color] -= 1
                if color_count[prev_color] == 0:
                    del color_count[prev_color]
                    curr -= 1

            balls[ball] = color
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1
                curr += 1

            result.append(curr)

        return result


        

if __name__ == '__main__':
    sys.exit(main())