from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(0, n-2):
            if nums[i] == 0:
                result += 1
                nums[i] = 1
                nums[i+ 1] = 1 - nums[i+1]
                nums[i+ 2] = 1 - nums[i+2]
        if nums[-1] == 1 and nums[-2] == 1:
            return result
        return -1
