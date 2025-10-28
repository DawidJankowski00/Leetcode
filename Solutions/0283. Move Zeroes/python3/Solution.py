from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        l = 0
        
        for r in range(n):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
            
