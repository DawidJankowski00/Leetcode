from collections import defaultdict
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            tmp = nums[l] + nums[r]
            if tmp == k:
                result += 1
                l += 1
                r -= 1
                continue
            if tmp >= k:
                r -= 1
            else:
                l += 1
        return result
