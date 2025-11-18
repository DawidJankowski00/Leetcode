from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        result = 0
        paired = sorted(zip(nums1, nums2), key=itemgetter(1), reverse=True)
        heap = []
        current_sum = 0
        for a, b in paired:
            current_sum += a
            heapq.heappush(heap, a)
            if len(heap) == k:
                result = max(result, current_sum * b)
                current_sum -= heapq.heappop(heap)

        return result