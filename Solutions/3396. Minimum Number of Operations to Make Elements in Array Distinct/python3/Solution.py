from typing import Counter, List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ht = set()
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in ht:
                return i // 3 + 1
            ht.add(nums[i])
        return 0
