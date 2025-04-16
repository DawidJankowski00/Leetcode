from collections import defaultdict
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.countGood([1,1,1,1,1], 10))
    print(time.time() - start)

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        result = 0
        n = len(nums)
        l = 0
        curr = defaultdict(int)
        curr_pairs = 0
        for r in range(0, n):
            curr_pairs += curr[nums[r]]
            curr[nums[r]] += 1
            
            while curr_pairs >= k and l < r:
                result += n - r
                curr[nums[l]] -= 1
                curr_pairs -= curr[nums[l]] 
                l += 1
        return result
if __name__ == '__main__':
    sys.exit(main())