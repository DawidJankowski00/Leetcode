from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = max(piles)

        while left<=right:
            mid  = (left+right)//2
            hour = 0
            
            for p in piles:
                hour = hour + (p+mid-1)//mid

            if hour > h:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1

        return ans
    
    