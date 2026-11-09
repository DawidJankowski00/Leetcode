import sys
from typing import List
def main():
    sol = Solution()
    print(sol.minSubArrayLen(11, [1,2,3,4,5]))

class Solution:
    def minSubArrayLen(self, k: int, nums: List[int]) -> int:
        if sum(nums) < k: return 0 
        result = len(nums)
        l = 0
        tmp = 0
        curr = 0

        for r,val in enumerate(nums):
            tmp+= val
            while tmp >= k:
                tmp-= nums[l]
                result = min(result, r - l + 1)
                l+= 1
        return result


        

if __name__ == '__main__':
    sys.exit(main())