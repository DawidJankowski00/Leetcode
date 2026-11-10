from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 1_000_000_007
        curr = 0
        ct = 0
        for v in arr:
            curr += v
            ct += curr % 2
        ct += (len(arr) - ct) * ct
        return ct % mod
