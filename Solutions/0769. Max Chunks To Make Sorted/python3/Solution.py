from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        curr = 0
        needed_sum = 0
        result = 0
        for i in range(n):
            needed_sum += i
            curr += arr[i]
            if needed_sum == curr:
                result += 1
        return result
