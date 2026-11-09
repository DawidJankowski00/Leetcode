from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxwather = 0
        while l != r:
            maxwather = max(maxwather, min(height[l], height[r]) * (r-l))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return maxwather
    
