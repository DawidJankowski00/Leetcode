from heapq import heapify, heappop, heappush
from math import isqrt
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.pickGifts([25,64,9,4,100], 4))
    print(time.time() - start)

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-x for x in gifts]
        i = 0
        x = 2
        while i<k and x>1:
            x=-heappop(gifts)
            heappush(gifts, -isqrt(x))
            i+=1
        return -sum(gifts)

if __name__ == '__main__':
    sys.exit(main())