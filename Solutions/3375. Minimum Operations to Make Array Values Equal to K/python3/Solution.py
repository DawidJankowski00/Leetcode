import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.minOperations([5,2,5,4,5],2))
    print(time.time() - start)

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        result = len(set(nums)) + (min(nums) > k) - 1
        return result
        

if __name__ == '__main__':
    sys.exit(main())