from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        result = []
        prefix = [0]
        c = 0
        for i in range(1, len(nums)):
            prefix.append(prefix[-1])
            if (nums[i-1] + nums[i]) % 2 == 0:
                prefix[i] += 1
        for l, r in queries:
            result.append(prefix[r]-prefix[l] == 0)
        return result
