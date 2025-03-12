import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.maximumCount([-2,-1,-1,1,2,3]))
    print(time.time() - start)

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        i = 0
        while i < n and nums[i] <= 0:
            if nums[i] != 0:
                l += 1
            i += 1
        return max(l, n-i)

if __name__ == '__main__':
    sys.exit(main())