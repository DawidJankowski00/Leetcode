from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) -1
        result = 0
        while l != r:
            if nums[l] + nums[r] <= upper:
                result += r - l
                l += 1
            else:
                r -= 1 
        l = 0
        r = len(nums) -1
        while l != r:
            if nums[l] + nums[r] < lower:
                result -= r - l
                l += 1
            else:
                r -= 1 
        return result
