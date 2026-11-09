from typing import Counter, List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        tab = Counter(nums)
        for v in tab.values():
            if v % 2 == 1:
                return False
        return True
