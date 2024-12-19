import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.maxChunksToSorted([4,3,2,1,0]))
    print(time.time() - start)

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        curr = 0
        needed_sum = 0
        result = 0
        for i in range(n):
            needed_sum += i
            curr += arr[i]
            if needed_sum == curr:
                result += 1
        return result
        

if __name__ == '__main__':
    sys.exit(main())