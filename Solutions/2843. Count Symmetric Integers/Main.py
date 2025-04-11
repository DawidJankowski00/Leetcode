import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.countSymmetricIntegers(1, 100))
    print(time.time() - start)

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        for i in range(low, high+1):
            tmp = str(i)
            n = len(tmp)
            if n % 2 == 1:
                continue
            a = 0
            b = 0
            n = n//2
            for j in range(0, n):
                a += int(tmp[j])
                b += int(tmp[j+n])
            if a == b:
                result += 1
        return result
        

if __name__ == '__main__':
    sys.exit(main())