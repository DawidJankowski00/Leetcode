from collections import Counter
import heapq
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.repeatLimitedString("cczazcc",3))
    print(time.time() - start)

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        result = ""
        last = -1
        hp = [(-ord(k), v) for k, v in Counter(s).items()] 
        heapq.heapify(hp)
        while hp:
            k, v = heapq.heappop(hp)
            if k == last:
                if hp:
                    kk, vv = heapq.heappop(hp)
                    result += chr(-kk)
                    if vv != 1:
                        heapq.heappush(hp, (kk, vv-1))
                    heapq.heappush(hp, (k, v))
                    last = kk
                else:
                    break
            else:
                if v > repeatLimit:
                    for _ in range(repeatLimit):
                        result += chr(-k)
                    heapq.heappush(hp, (k, v - repeatLimit))
                else:
                    for _ in range(v):
                        result += chr(-k)
                last = k
        return result
        

if __name__ == '__main__':
    sys.exit(main())