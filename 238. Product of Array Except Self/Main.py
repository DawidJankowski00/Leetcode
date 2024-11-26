import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.productExceptSelf([2,3,4,5,6]))
    print(time.time() - start)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range(1, len(nums)):
            left.append(left[i-1]*nums[i-1])
        right = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
            left[i] *= right[i]
        return left

        

if __name__ == '__main__':
    sys.exit(main())