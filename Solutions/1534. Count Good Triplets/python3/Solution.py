import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.countGoodTriplets([1,1,2,2,3],0,0,1))
    print(time.time() - start)

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        result = 0
        n = len(arr)
        for i in range(0,n-2):
            for j in range(i+1, n-1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j+1, n):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            result += 1
        return result
if __name__ == '__main__':
    sys.exit(main())