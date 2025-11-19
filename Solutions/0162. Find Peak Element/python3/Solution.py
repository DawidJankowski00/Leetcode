from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        first = 0
        n = len(nums)-1
        while first < n:
            mid = first + (n - first + 1) // 2
            if nums[mid] < nums[mid-1]:
                n = mid - 1
            else:
                first = mid
        return first