import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()

    print(sol.canJump([2,3,1,1,4]))
    print(time.time() - start)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        for i in nums:
            if start < 0:
                return False
            if start < i:
                start = i
            start -= 1
        return True
            

if __name__ == '__main__':
    sys.exit(main())

