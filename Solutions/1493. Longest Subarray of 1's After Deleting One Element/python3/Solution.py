from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        k = 1
        n = len(nums)
        for r in range(n):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l