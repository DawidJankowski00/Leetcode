from collections import defaultdict
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.countBadPairs([4,1,3,3]))
    print(time.time() - start)

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        result = (n * (n - 1)) // 2
        freq = {}
        for i in range(0, n):
            tmp = nums[i] - i
            result -= freq.get(tmp,0)
            freq[tmp] = freq.get(tmp,0) + 1
        return result
        

if __name__ == '__main__':
    sys.exit(main())