from functools import reduce
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.subsetXORSum([5,1,6]))
    print(time.time() - start)

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return reduce(or_, nums) << (len(nums)-1)
        

if __name__ == '__main__':
    sys.exit(main())