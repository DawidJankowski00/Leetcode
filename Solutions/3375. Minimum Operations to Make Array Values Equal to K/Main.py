import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.minOperations([5,2,5,4,5],2))
    print(time.time() - start)

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        result = 0
        if nums[-1] < k:
            return -1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                result += 1
        if nums[-1] != k:
            result += 1
        return result
        

if __name__ == '__main__':
    sys.exit(main())