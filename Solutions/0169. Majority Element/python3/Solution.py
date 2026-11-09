from collections import defaultdict
import sys
from typing import List
def main():
    sol = Solution()
    print(sol.majorityElement([2,2,1,1,1,2,2]))

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        table = defaultdict(int)
        for el in nums:
            table[el] += 1

        n = len(nums) // 2
        for key, value in table.items():
            if value > n:
                return key

if __name__ == '__main__':
    sys.exit(main())