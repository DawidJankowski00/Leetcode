from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = 1
        result = [1] * n
        for i in range(n):
            result[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(n-1, -1, -1):
            result[i] *= post
            post *= nums[i]
        return result