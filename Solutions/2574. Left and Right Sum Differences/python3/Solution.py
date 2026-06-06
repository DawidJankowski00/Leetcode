class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l = 0
        r = sum(nums)
        r -= nums[0]
        result = []
        result.append(r)

        for i in range(1, len(nums)):
            l += nums[i-1]
            r -= nums[i]
            result.append(abs(l - r))

        return result