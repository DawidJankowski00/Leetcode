class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        result = max(nums) - min(nums)
        return k * result