import sys
import time
from typing import Counter, List

def main():
    sol = Solution()
    start = time.time()
    print(sol.divideArray([3,2,3,2,2,2]))
    print(time.time() - start)

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        tab = Counter(nums)
        for v in tab.values():
            if v % 2 == 1:
                return False
        return True
        

if __name__ == '__main__':
    sys.exit(main())