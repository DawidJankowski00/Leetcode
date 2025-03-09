import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.numberOfAlternatingGroups([0,1,0,1,0], 3))
    print(time.time() - start)

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors = colors + colors[:(k-1)]
        result = 0
        l = 0
        for r in range(len(colors)):
            if colors[r] == colors[r-1]:
                l = r
            if r-l >= k-1:
                result += 1
        return result
        

if __name__ == '__main__':
    sys.exit(main())