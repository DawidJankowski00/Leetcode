import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.maxCount([1,6,5],5,7))
    print(time.time() - start)

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        dic = set(banned)
        csum = 0
        nums = 0
        for i in range(1, n+1):
            if i in dic:
                continue
            csum += i
            if csum > maxSum:
                break
            nums += 1
        return nums

        

if __name__ == '__main__':
    sys.exit(main())