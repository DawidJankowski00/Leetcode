import sys
from typing import List
def main():
    sol = Solution()
    print(sol.removeElement([1,1,2]))

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

if __name__ == '__main__':
    sys.exit(main())