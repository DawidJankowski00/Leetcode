import math
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l1 = math.inf
        l2 = math.inf
        for v in nums:
            if v <= l1:
                l1 = v
            elif v <= l2:
                l2 = v
            else:
                return True
        return False
