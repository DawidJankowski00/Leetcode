import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.twoSum([2,7,11,15], 7))
    print(time.time() - start)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l != r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l +=1
        

if __name__ == '__main__':
    sys.exit(main())