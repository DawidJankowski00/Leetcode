import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.minOperations([[2,4],[6,8]],2))
    print(time.time() - start)

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        values = []
        for v in grid:
            values += v
        tmp = values[0] % x
        for v in values:
            if v % x == tmp:
                continue
            else:
                return -1
        values.sort()
        median = values[len(values)//2]
        result = 0
        for v in values:
            result += abs(median - v) // x
        return result
        
        

if __name__ == '__main__':
    sys.exit(main())