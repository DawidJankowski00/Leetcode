from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr = 0
        maxcurr = 0
        mincurr = 0
        for v in nums:
            curr += v
            maxcurr = max(curr, maxcurr)
            mincurr = min(curr, mincurr)
        return abs(maxcurr - mincurr)
