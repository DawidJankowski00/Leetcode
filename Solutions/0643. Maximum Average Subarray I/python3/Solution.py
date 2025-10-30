from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        result = curr
        n = len(nums)
        for i in range(k, n):
            curr += nums[i]
            curr -= nums[i-k]
            if result < curr:
                result = curr
        return result/k
            
