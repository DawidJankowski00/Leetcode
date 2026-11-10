from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        l = 0
        last = 0
        if len(nums) == 0:
            return []
        for i in range(1, len(nums)):
            if nums[i] == nums[last] + 1:
                last = i
            else:
                if last - l == 0:
                    result.append(str(nums[l]))
                else:
                    result.append(str(nums[l]) + "->" + str(nums[last]))
                l = i
                last = i
        if last - l == 0:
            result.append(str(nums[l]))
        else:
            result.append(str(nums[l]) + "->" + str(nums[last]))
        return result
