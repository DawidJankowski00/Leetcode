from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        curr = 0
        for v in gain:
            curr += v
            if curr > result:
                result = curr
        return result