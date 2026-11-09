import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.countPairs([3,1,2,2,2,1,3],2))
    print(time.time() - start)

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        for i in range(0, n-1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    if (i * j) % k == 0:
                        result += 1
        return result
        

if __name__ == '__main__':
    sys.exit(main())