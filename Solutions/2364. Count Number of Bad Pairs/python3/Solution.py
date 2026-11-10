from collections import defaultdict
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        result = (n * (n - 1)) // 2
        freq = {}
        for i in range(0, n):
            tmp = nums[i] - i
            result -= freq.get(tmp,0)
            freq[tmp] = freq.get(tmp,0) + 1
        return result
