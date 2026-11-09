from collections import defaultdict
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.tupleSameProduct([2,3,4,6]))
    print(time.time() - start)

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        freq = defaultdict(int)
        for i in range(n):
            for j in range(i+1, n):
                tmp = nums[i] * nums[j]
                result += freq[tmp]
                freq[tmp] += 1
        return result*8
        

if __name__ == '__main__':
    sys.exit(main())