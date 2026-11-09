from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        start = prices[0]
        for i in range(0 , len(prices)):
            if start < prices[i]: 
                max += prices[i] - start
            start = prices[i]
        return max
