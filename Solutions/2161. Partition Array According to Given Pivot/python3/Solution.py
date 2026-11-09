from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lower = []
        equal = []
        greather = []
        for v in nums:
            if v < pivot:
                lower.append(v)
            elif v == pivot:
                equal.append(v)
            else:
                greather.append(v)
        return lower + equal + greather
