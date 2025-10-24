from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        result = []

        for v in candies:
            if v + extraCandies >= m:
                result.append(True)
            else:
                result.append(False)

        return result