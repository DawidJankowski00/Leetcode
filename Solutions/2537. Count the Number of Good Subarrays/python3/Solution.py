from collections import defaultdict
from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        result = 0
        n = len(nums)
        l = 0
        curr = defaultdict(int)
        curr_pairs = 0
        for r in range(0, n):
            curr_pairs += curr[nums[r]]
            curr[nums[r]] += 1
            
            while curr_pairs >= k and l < r:
                result += n - r
                curr[nums[l]] -= 1
                curr_pairs -= curr[nums[l]] 
                l += 1
        return result
