from typing import List
from collections import Counter, defaultdict

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        right = Counter(nums)
        left = defaultdict(int)
        l_n = 0
        r_n = len(nums)
        element = max(right, key=right.get)
        if right[element] * 2 <= r_n:
            return -1
        for i in range(len(nums)):
            l_n += 1
            r_n -= 1
            left[nums[i]] += 1
            right[nums[i]] -= 1
            if left[element] * 2 > l_n and right[element] * 2 > r_n:
                return i
        return -1
