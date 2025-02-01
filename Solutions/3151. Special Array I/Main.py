import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.isArraySpecial([4,3,1,6]))
    print(time.time() - start)

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] % 2 == nums[i] % 2:
                return False
        return True
        

if __name__ == '__main__':
    sys.exit(main())