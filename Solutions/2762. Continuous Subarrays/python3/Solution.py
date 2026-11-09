import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.continuousSubarrays([5,4,2,4]))
    print(time.time() - start)

class Solution:
    def continuousSubarrays(self, nums):
        l, r, j = 0, 0, 0
        result = 0

        for i in range(len(nums)):
            if i == 0:
                result += 1
                l = nums[i] - 2
                r = nums[i] + 2
            elif l <= nums[i] <= r:
                l = max(l, nums[i] - 2)
                r = min(r, nums[i] + 2)
                result += (i - j + 1)
            else:
                j = i - 1
                l, r = nums[i] - 2, nums[i] + 2

                while j >= 0 and nums[j] >= nums[i] - 2 and nums[j] <= nums[i] + 2:
                    l = max(l, nums[j] - 2)
                    r = min(r, nums[j] + 2)
                    j -= 1

                j += 1
                result += (i - j + 1)

        return result


if __name__ == '__main__':
    sys.exit(main())