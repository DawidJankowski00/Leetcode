import sys
from typing import List
def main():
    sol = Solution()
    print(sol.removeDuplicates([1,1,1]))

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in nums:
            if k < 2 or i != nums[k - 2]:
                nums[k] = i
                k += 1
        return k 

if __name__ == '__main__':
    sys.exit(main())