from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tmp = nums[j] + nums[k] + nums[i]
                if tmp == 0:
                    result.append((nums[j],nums[i],nums[k]))
                    j += 1
                    k -= 1 
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif tmp > 0:
                    k -= 1
                else:
                    j += 1
        return result
