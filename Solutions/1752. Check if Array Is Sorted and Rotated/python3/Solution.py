from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        result = sorted(nums)
        for i in range(0, n):
            tmp = nums[i:] + nums[:i]
            if result == tmp:
                return True
        return False
