import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1],2))
    print(time.time() - start)

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sub1, sub2, sub3 = sum(nums[:k]), sum(nums[k:2*k]), sum(nums[2*k:3*k])
        sub1_index, sub2_index, sub3_index = [0], [0, k], [0, k, 2*k]
        sum1, sum2, sum3 = sub1, sub1 + sub2, sub1 + sub2 + sub3

        for i in range(1, len(nums)-3*k +1):
            sub1 += nums[i - 1 + k] - nums[i - 1]
            sub2 += nums[i - 1 + k*2] - nums[i - 1 + k]
            sub3 += nums[i - 1 + k*3] - nums[i - 1 + 2*k]

            if sub1 > sum1:
                sum1 = sub1
                sub1_index = [i]
            if sum1 + sub2 > sum2:
                sum2 = sum1 + sub2
                sub2_index = sub1_index + [i + k]
            if sum2 + sub3 > sum3:
                sum3 = sum2 + sub3
                sub3_index = sub2_index + [i + 2*k]
        return sub3_index

if __name__ == '__main__':
    sys.exit(main())