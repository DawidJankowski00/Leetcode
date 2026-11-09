from collections import defaultdict
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.twoSum([2,7,11,15],9))
    print(time.time() - start)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        for i, v in enumerate(nums):
            if target - v in dic:
                return [dic[target-v], i]
            dic[v] = i

if __name__ == '__main__':
    sys.exit(main())