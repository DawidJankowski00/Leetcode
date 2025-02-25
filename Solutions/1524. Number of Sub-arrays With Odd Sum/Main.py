import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.numOfSubarrays([1,2,3,4,5,6,7]))
    print(time.time() - start)

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 1_000_000_007
        curr = 0
        ct = 0
        for v in arr:
            curr += v
            ct += curr % 2
        ct += (len(arr) - ct) * ct
        return ct % mod
        

if __name__ == '__main__':
    sys.exit(main())