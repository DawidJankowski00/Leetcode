import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.check([3,4,5,1,2]))
    print(time.time() - start)

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        result = sorted(nums)
        for i in range(0, n):
            tmp = nums[i:] + nums[:i]
            if result == tmp:
                return True
        return False
        

if __name__ == '__main__':
    sys.exit(main())