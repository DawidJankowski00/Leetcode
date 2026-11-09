from heapq import heapify, heappop, heappush
from math import isqrt
from typing import List

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
