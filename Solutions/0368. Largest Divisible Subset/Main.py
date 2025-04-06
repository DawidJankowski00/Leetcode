import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.largestDivisibleSubset([1,2,4,8]))
    print(time.time() - start)

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [[v] for v in nums]
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)
        

if __name__ == '__main__':
    sys.exit(main())