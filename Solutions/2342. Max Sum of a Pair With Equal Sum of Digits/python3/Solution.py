from collections import defaultdict
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.maximumSum([10,12,19,14]))
    print(time.time() - start)

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        result = -1
        map = defaultdict(int)
        for i, num in enumerate(nums):
            tmp = num
            Digits_sum = 0
            while tmp >= 10:
                Digits_sum += tmp % 10
                tmp //= 10
            Digits_sum += tmp
            if Digits_sum in map:
                tmp = map[Digits_sum]
                if result < tmp + num:
                    result = tmp + num
                if tmp < num:
                    map[Digits_sum] = num
            else:
                map[Digits_sum] = num
        return result
        

if __name__ == '__main__':
    sys.exit(main())