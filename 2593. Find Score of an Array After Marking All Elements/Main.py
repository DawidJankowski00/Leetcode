import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.findScore([2,1,3,4,5,2]))
    print(time.time() - start)

class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted((num, idx) for idx, num in enumerate(nums))
        result = 0
        for num, i in sorted_nums:
            if nums[i] != -1:
                result += num
                nums[i] = -1
                if i > 0:
                    nums[i-1] = -1
                if i < n-1:
                    nums[i+1] = -1
        return result
        

if __name__ == '__main__':
    sys.exit(main())