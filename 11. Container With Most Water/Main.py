import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
    print(time.time() - start)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxAmount = 0
        while l != r:
            if maxAmount < min(height[l], height[r]) * (r-l):
                maxAmount = min(height[l], height[r]) * (r-l)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxAmount
   
        

if __name__ == '__main__':
    sys.exit(main())