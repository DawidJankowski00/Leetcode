import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.longestMonotonicSubarray([3,2,1]))
    print(time.time() - start)

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        tmp_dec = 1
        tmp_inc = 1
        for i in range(1,n):
            if nums[i-1] < nums[i]:
                tmp_dec += 1
            else:
                if tmp_dec > result:
                    result = tmp_dec
                tmp_dec = 1
            if nums[i-1] > nums[i]:
                tmp_inc += 1
            else:
                if tmp_inc > result:
                    result = tmp_inc
                tmp_inc = 1
        return max(result, tmp_dec, tmp_inc)
        

if __name__ == '__main__':
    sys.exit(main())