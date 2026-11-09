from collections import defaultdict
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.isHappy(19))
    print(time.time() - start)

class Solution:
    def isHappy(self, n: int) -> bool:
        dic  = defaultdict(int)
        while n not in dic:
            if n == 1:
                return True
            dic[n] = 0
            tmp = 0
            while n != 0:
                tmp += (n%10) ** 2
                n -= n%10
                n = n // 10
            n = tmp
        return False
        

if __name__ == '__main__':
    sys.exit(main())