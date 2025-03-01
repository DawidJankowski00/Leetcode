import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.applyOperations([1,2,2,1,1,0]))
    print(time.time() - start)

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        result = []
        z = 0
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] *= 2
                nums[i] = 0
            if nums[i-1] != 0:
                result.append(nums[i-1])
            else:
                z += 1
        if nums[-1] == 0:
            z += 1
        else:
            result.append(nums[-1])
        for i in range(0, z):
            result.append(0)
        return result
        

if __name__ == '__main__':
    sys.exit(main())