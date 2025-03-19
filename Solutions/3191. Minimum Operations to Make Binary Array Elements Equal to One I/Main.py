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
        l = 0
        r = 2
        result = 0
        while r < n:
            if nums[l] == 1:
                l += 1
                r += 1
            else:
                result += 1
                for i in range(l, r+1):
                    if nums[i] == 0:
                        nums[i] = 1
                    else:
                        nums[i] = 0
        if nums[-1] == 1 and nums[-2] == 1:
            return result
        return -1

if __name__ == '__main__':
    sys.exit(main())