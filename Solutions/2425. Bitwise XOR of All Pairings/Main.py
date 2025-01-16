import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.xorAllNums([2,1,3],[10,2,5,0]))
    print(time.time() - start)

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        result2 = 0
        n = len(nums1)
        m = len(nums2)
        if n % 2 == 1:
            for v in nums2:
                result2 ^= v
        if m %2 == 1:
            for v in nums1:
                result ^= v
        return result ^ result2
        

if __name__ == '__main__':
    sys.exit(main())