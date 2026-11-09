from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        for l in range(n):
            r = l + 1
            while r < n:
                if prices[l] >= prices[r]:
                    prices[l] -= prices[r]
                    break
                else:
                    r += 1
        return prices
