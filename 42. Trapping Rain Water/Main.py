import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.trap([2,1,0,1,3,2]))
    print(time.time() - start)

class Solution:
    def trap(self, height: List[int]) -> int:
        r = len(height) - 1
        l = 0
        maxleft = height[l]
        maxright = height[r]
        water = 0
        while r != l:
            if height[r] <= height[l]:
                r -= 1
                if maxright < height[r]:
                    maxright = height[r]
                water += maxright - height[r]
            else:
                l += 1
                if maxleft < height[l]:
                    maxleft = height[l]
                water += maxleft - height[l] 
        return water

        

if __name__ == '__main__':
    sys.exit(main())