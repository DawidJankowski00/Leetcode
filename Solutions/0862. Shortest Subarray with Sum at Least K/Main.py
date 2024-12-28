import sys
from typing import List
def main():
    sol = Solution()
    print(sol.shortestSubarray([2,-1,2], 3))

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)+1):
            for j in range(0, len(nums)-i+1):
                if sum(nums[j:j+i]) >= k:
                    return i
        return -1

            


        

if __name__ == '__main__':
    sys.exit(main())