from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        tmp = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                tmp += nums[i]
            else:
                result = max(result, tmp)
                tmp = nums[i]
        return max(result, tmp)
