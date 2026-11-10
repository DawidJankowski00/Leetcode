from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        for i in nums:
            if start < 0:
                return False
            if start < i:
                start = i
            start -= 1
        return True
