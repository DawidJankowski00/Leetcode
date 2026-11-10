from collections import defaultdict
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        freq = defaultdict(int)
        for i in range(n):
            for j in range(i+1, n):
                tmp = nums[i] * nums[j]
                result += freq[tmp]
                freq[tmp] += 1
        return result*8
