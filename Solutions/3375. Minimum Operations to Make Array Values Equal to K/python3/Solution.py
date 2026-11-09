from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        result = len(set(nums)) + (min(nums) > k) - 1
        return result
