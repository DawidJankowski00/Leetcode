import sys
import time
from typing import Counter, List
def main():
    sol = Solution()
    start = time.time()
    print(sol.minimumOperations([1,2,3,4,2,3,3,5,7]))
    print(time.time() - start)

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ht = Counter(nums)
        bad = 0
        for v in ht.values():
            if v != 1:
                bad += 1
        result = 0
        while len(nums) > 3:
            if bad == 0:
                return result
            for i in range(0, 3):
                if ht[nums[i]] == 2:
                    bad -= 1
                ht[nums[i]] -= 1
            result += 1
            nums = nums[3:]
        if bad != 0:
            return result + 1
        return result
        

if __name__ == '__main__':
    sys.exit(main())