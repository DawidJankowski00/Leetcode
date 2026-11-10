from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        i = 0
        while i < n and nums[i] <= 0:
            if nums[i] != 0:
                l += 1
            i += 1
        return max(l, n-i)
