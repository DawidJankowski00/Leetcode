import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.countSubarrays([1,2,1,4,1]))
    print(time.time() - start)

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(0, n - 2):
            if (nums[i] + nums[i+2]) * 2 == nums[i+1]:
                result += 1
        return result

if __name__ == '__main__':
    sys.exit(main())