import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()

    print(sol.maxProfit([7,1,5,3,6,4]))
    print(time.time() - start)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        start = prices[0]
        for i in range(0 , len(prices)):
            if start < prices[i]: 
                max += prices[i] - start
            start = prices[i]
        return max
            

if __name__ == '__main__':
    sys.exit(main())

