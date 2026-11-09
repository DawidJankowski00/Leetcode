import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.maxAbsoluteSum([2,-5,1,-4,3,-2]))
    print(time.time() - start)

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr = 0
        maxcurr = 0
        mincurr = 0
        for v in nums:
            curr += v
            maxcurr = max(curr, maxcurr)
            mincurr = min(curr, mincurr)
        return abs(maxcurr - mincurr)

if __name__ == '__main__':
    sys.exit(main())