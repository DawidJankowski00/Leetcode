import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.minOperations([0,1,1,1,0,0]))
    print(time.time() - start)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(0, n-2):
            if nums[i] == 0:
                result += 1
                nums[i] = 1
                nums[i+ 1] = 1 - nums[i+1]
                nums[i+ 2] = 1 - nums[i+2]
        if nums[-1] == 1 and nums[-2] == 1:
            return result
        return -1

if __name__ == '__main__':
    sys.exit(main())