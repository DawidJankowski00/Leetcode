import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.isArraySpecial([4,3,1,6], [[0,2],[2,3]]))
    print(time.time() - start)

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        result = []
        prefix = [0]
        c = 0
        for i in range(1, len(nums)):
            prefix.append(prefix[-1])
            if (nums[i-1] + nums[i]) % 2 == 0:
                prefix[i] += 1
        for l, r in queries:
            result.append(prefix[r]-prefix[l] == 0)
        return result

if __name__ == '__main__':
    sys.exit(main())