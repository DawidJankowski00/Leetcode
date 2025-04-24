import sys
import time
from typing import Counter, List
def main():
    sol = Solution()
    start = time.time()
    print(sol.countCompleteSubarrays([1,3,1,2,2]))
    print(time.time() - start)

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        all = Counter(nums)
        all_ct = len(all)
        n = len(nums)
        result = 0
        curr = Counter()
        l = 0
        for r in range(0, n):
            curr[nums[r]] += 1
            while len(curr) == all_ct:
                curr[nums[l]] -= 1
                if curr[nums[l]] == 0:
                    del curr[nums[l]]
                l += 1
                result += n - r
        return result

if __name__ == '__main__':
    sys.exit(main())