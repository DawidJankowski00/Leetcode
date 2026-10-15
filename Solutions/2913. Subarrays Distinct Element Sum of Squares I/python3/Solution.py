class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(0, n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                tmp = len(seen)
                result += tmp ** 2
        return result

        