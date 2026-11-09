import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(time.time() - start)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elems = sorted(set(nums))
        result = 0
        last = None
        tmp = 0
        for el in elems:
            if el - 1 == last:
                tmp += 1
            else:
                if result < tmp:
                    result = tmp
                tmp = 1
            last = el
        if result < tmp:
            result = tmp
        return result
        

if __name__ == '__main__':
    sys.exit(main())