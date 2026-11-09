from typing import Counter, List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        all = Counter(nums)
        all_ct = len(all)
        n = len(nums)
        result = 0
        curr = Counter()
        l = 0
        for r in range(0, n):
            curr[nums[r]] += 1
            while len(curr) == all_ct:
                curr[nums[l]] -= 1
                if curr[nums[l]] == 0:
                    del curr[nums[l]]
                l += 1
                result += n - r
        return result
