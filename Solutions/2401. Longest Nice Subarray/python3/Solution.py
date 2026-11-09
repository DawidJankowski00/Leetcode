from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        result = 1
        curr = nums[0]
        l = 0
        r = 1
        n = len(nums)
        while r < n:
            if curr & nums[r] == 0:
                curr += nums[r]
                r += 1
            else:
                result = max(r-l, result)
                curr -= nums[l]
                l += 1 
        result = max(result, r-l)
        return result
