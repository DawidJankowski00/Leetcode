class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums) // 2
        nums.sort()
        tmp = nums[n]
        result = 0
        for v in nums[:n]:
            result += tmp - v
        for v in nums[n:]:
            result += v - tmp
        return result
        