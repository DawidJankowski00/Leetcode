from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        result = 0
        cur_sum_r = sum(nums)
        cur_sum_l = 0
        for i in range(0, len(nums)-1):
            cur_sum_r -= nums[i]
            cur_sum_l += nums[i]
            if cur_sum_l >= cur_sum_r:
                result += 1
        return result
