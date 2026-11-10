from typing import List
import heapq

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
