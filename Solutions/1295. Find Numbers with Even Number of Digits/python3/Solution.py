import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.findNumbers([12,345,2,6,7896]))
    print(time.time() - start)

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for v in nums:
            if len(str(v)) % 2 == 0:
                result += 1
        return result
        

if __name__ == '__main__':
    sys.exit(main())