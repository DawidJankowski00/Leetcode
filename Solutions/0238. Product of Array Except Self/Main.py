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
        n = len(nums)
        pre = 1
        result = [1] * n
        for i in range(n):
            result[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(n-1, -1, -1):
            result[i] *= post
            post *= nums[i]
        return result

        

if __name__ == '__main__':
    sys.exit(main())