import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.countFairPairs([0,1,7,4,4,5], 3, 6))
    print(time.time() - start)

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) -1
        result = 0
        while l != r:
            if nums[l] + nums[r] <= upper:
                result += r - l
                l += 1
            else:
                r -= 1 
        l = 0
        r = len(nums) -1
        while l != r:
            if nums[l] + nums[r] < lower:
                result -= r - l
                l += 1
            else:
                r -= 1 
        return result
        

if __name__ == '__main__':
    sys.exit(main())