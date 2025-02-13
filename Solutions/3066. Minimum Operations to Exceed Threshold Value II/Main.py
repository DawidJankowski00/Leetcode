import sys
import time
from typing import List
import heapq
def main():
    sol = Solution()
    start = time.time()
    print(sol.minOperations([2,11,10,1,3],10))
    print(time.time() - start)

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = 0
        heapq.heapify(nums)
        a = heapq.heappop(nums)
        while a < k:
            result += 1
            heapq.heappush(nums, a * 2 + heapq.heappop(nums))
            a = heapq.heappop(nums)
        return result

if __name__ == '__main__':
    sys.exit(main())