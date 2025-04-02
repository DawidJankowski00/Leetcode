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
        result = 0
        for i in range(0,n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    result = max(result, ((nums[i] - nums[j]) * nums[k]))
        return result

if __name__ == '__main__':
    sys.exit(main())