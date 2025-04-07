import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.canPartition([1,5,11,5]))
    print(time.time() - start)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for v in nums:
            for i in range(target, v-1, -1):
                dp[i] = dp[i] or dp[i-v]
        return dp[target]

        

if __name__ == '__main__':
    sys.exit(main())