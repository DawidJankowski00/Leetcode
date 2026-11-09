from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        maxvalue = 0
        maxdiff = 0
        result = 0
        for i in range(0, n):
            result = max(result, maxdiff * nums[i])
            maxdiff = max(maxdiff, maxvalue - nums[i])
            maxvalue = max(maxvalue, nums[i])

        return result
