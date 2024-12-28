import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.finalPrices([8,4,6,2,3]))
    print(time.time() - start)

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
        

if __name__ == '__main__':
    sys.exit(main())