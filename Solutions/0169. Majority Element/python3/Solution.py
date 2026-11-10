from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        table = defaultdict(int)
        for el in nums:
            table[el] += 1

        n = len(nums) // 2
        for key, value in table.items():
            if value > n:
                return key
