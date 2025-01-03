import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.waysToSplitArray([10,4,-8,7]))
    print(time.time() - start)

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        result = 0
        cur_sum_r = sum(nums)
        cur_sum_l = 0
        for i in range(0, len(nums)-1):
            cur_sum_r -= nums[i]
            cur_sum_l += nums[i]
            if cur_sum_l >= cur_sum_r:
                result += 1
        return result
    
if __name__ == '__main__':
    sys.exit(main())