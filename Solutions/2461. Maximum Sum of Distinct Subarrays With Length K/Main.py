import sys
from typing import List
def main():
    sol = Solution()
    print(sol.maximumSubarraySum([1,5,4,2,9,9,9], 3))

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxValue = 0
        currentValue = sum(nums[0:k])
        mapHas = {}
        for i in range(k):
            if nums[i] in mapHas:
                mapHas[nums[i]] += 1
            else:
                mapHas[nums[i]] = 1
        if len(mapHas) == k:
            if maxValue < currentValue:
                maxValue = currentValue
        for i in range(0, len(nums)-k):
            currentValue -= nums[i]
            currentValue += nums[i+k]
            mapHas[nums[i]] -= 1
            if nums[i+k] in mapHas:
                mapHas[nums[i+k]] += 1
            else:
                mapHas[nums[i+k]] = 1
            if mapHas[nums[i]] == 0:
                del mapHas[nums[i]]

            if len(mapHas) == k:
                if maxValue < currentValue:
                    maxValue = currentValue
        return maxValue
        

if __name__ == '__main__':
    sys.exit(main())