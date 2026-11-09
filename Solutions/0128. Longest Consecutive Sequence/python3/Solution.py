from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elems = sorted(set(nums))
        result = 0
        last = None
        tmp = 0
        for el in elems:
            if el - 1 == last:
                tmp += 1
            else:
                if result < tmp:
                    result = tmp
                tmp = 1
            last = el
        if result < tmp:
            result = tmp
        return result
