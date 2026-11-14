class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        result = float('inf')
        n = len(nums)
        for i in range(l, r+1):
            curr = sum(nums[:i])
            if curr > 0:
                result = min(result, curr)
            for j in range(i, n):
                curr += nums[j]
                curr -= nums[j-i]
                if curr > 0:
                    result = min(result, curr)
        return result if result != float('inf') else -1