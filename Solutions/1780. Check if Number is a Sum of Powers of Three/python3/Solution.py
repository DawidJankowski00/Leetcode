import sys
import time
from typing import List
import numpy as np
def main():
    sol = Solution()
    start = time.time()
    print(sol.checkPowersOfThree(12))
    print(sol.checkPowersOfThree(91))
    print(sol.checkPowersOfThree(21))
    print(time.time() - start)

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n != 0:
            if n % 3 == 2:
                return False
            n = n // 3
        return True
        

if __name__ == '__main__':
    sys.exit(main())