from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        min = prices[0]
        for item in prices[1:]:
            if min > item:
                min = item
            if max < item - min:
                max = item - min
        return max
