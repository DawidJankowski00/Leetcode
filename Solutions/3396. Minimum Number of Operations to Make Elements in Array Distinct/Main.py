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
        ht = set()
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in ht:
                return i // 3 + 1
            ht.add(nums[i])
        return 0
        
        

if __name__ == '__main__':
    sys.exit(main())