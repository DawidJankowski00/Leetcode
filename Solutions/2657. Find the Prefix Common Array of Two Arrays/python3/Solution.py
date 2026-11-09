import sys
import time
from typing import List
from collections import defaultdict
def main():
    sol = Solution()
    start = time.time()
    print(sol.findThePrefixCommonArray([1,3,2,4],[3,1,2,4]))
    print(time.time() - start)

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        result = [0] * n
        nums = defaultdict(int)
        for i in range(n):
            result[i] = result[i-1]
            if A[i] == B[i]:
                result[i] += 1
            else:
                nums[A[i]] += 1
                nums[B[i]] += 1
                if nums[A[i]] == 2:
                    result[i] += 1
                if nums[B[i]] == 2:
                    result[i] += 1
        return result

        

if __name__ == '__main__':
    sys.exit(main())