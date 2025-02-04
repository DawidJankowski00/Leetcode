import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.maxAscendingSum([10,20,30,5,10,50]))
    print(time.time() - start)

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        tmp = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                tmp += nums[i]
            else:
                result = max(result, tmp)
                tmp = nums[i]
        return max(result, tmp)
        

if __name__ == '__main__':
    sys.exit(main())