import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.maximumTripletValue([12,6,1,2,7]))
    print(time.time() - start)

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        maxvalue = 0
        maxdiff = 0
        result = 0
        for i in range(0, n):
            result = max(result, maxdiff * nums[i])
            maxdiff = max(maxdiff, maxvalue - nums[i])
            maxvalue = max(maxvalue, nums[i])

        return result

if __name__ == '__main__':
    sys.exit(main())