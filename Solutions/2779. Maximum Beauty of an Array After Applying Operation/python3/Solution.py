import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.maximumBeauty([4,6,1,2], 2))
    print(time.time() - start)

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        r = 0
        for l in range(n):
            while r < n and nums[l] + (2* k) >= nums[r]:
                r += 1
                if result < r-l:
                    result = r-l
        return result

        

if __name__ == '__main__':
    sys.exit(main())