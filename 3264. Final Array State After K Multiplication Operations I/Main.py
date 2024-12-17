import heapq
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.getFinalState([2,1,3,5,6],5,2))
    print(time.time() - start)

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        for i, elem in enumerate(nums):
            heapq.heappush(heap, (elem, i))
        for _ in range(k):
            elem, i = heapq.heappop(heap)
            elem *= multiplier
            nums[i] = elem
            heapq.heappush(heap, (elem, i))
        return nums

if __name__ == '__main__':
    sys.exit(main())