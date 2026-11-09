import sys
from typing import List
def main():
    sol = Solution()
    print(sol.removeElement([3,2,2,3], 3))

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                del nums[i]
        print(nums)
        return len(nums)

if __name__ == '__main__':
    sys.exit(main())