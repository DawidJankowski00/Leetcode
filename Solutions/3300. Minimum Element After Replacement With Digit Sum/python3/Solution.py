class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = self.calc(nums[0])
        for v in nums[1:]:
            result = min(result, self.calc(v))
        return result

    def calc(self, v: int) -> int:

        result = 0
        while v > 0:
            result += v % 10
            v //= 10
        return result