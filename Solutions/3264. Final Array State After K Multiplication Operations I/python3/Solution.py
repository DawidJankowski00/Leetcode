import heapq
from typing import List

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
