from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for v in nums:
            if len(str(v)) % 2 == 0:
                result += 1
        return result
