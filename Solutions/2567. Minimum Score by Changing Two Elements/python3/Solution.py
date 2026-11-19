from heapq import nlargest, nsmallest
from typing import List


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return 0

        smallest = nsmallest(3, nums)
        largest = nlargest(3, nums)

        a = largest[0] - smallest[2]
        b = largest[1] - smallest[1]
        c = largest[2] - smallest[0]

        return min(a, b, c)