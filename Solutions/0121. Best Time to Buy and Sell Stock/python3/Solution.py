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
        min = prices[0]
        for item in prices[1:]:
            if min > item:
                min = item
            if max < item - min:
                max = item - min
        return max
            

if __name__ == '__main__':
    sys.exit(main())

