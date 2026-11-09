from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        r = 0
        for l in range(n):
            while r < n and nums[l] + (2* k) >= nums[r]:
                r += 1
                if result < r-l:
                    result = r-l
        return result
