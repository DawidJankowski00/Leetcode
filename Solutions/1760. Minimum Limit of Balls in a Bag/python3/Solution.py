from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)
        while l < r:
            mid = (r + l) // 2
            tmp = 0
            for a in nums:
                tmp += (a-1) // mid
            if tmp > maxOperations:
                l = mid + 1
            else:
                r = mid
        return l
