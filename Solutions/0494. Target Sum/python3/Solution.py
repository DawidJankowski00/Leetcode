import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.findTargetSumWays([1,1,1,1,1], 3))
    print(time.time() - start)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        tmp = 0
        self.memo = {}
        return self.helper(nums, target, n - 1, tmp)
    def helper(self, nums, target, n, tmp):
        if (n, tmp) in self.memo:
            return self.memo[(n,tmp)]
        if n < 0 and tmp == target:
            return 1
        if n < 0:
            return 0
        self.memo[(n, tmp)] = self.helper(nums, target, n-1, tmp + nums[n]) + self.helper(nums, target, n-1, tmp + -nums[n])
        return self.memo[(n, tmp)]

if __name__ == '__main__':
    sys.exit(main())