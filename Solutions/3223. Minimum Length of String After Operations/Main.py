import sys
import time
from typing import List
from collections import Counter
def main():
    sol = Solution()
    start = time.time()
    print(sol.minimumLength("abaacbcbb"))
    print(time.time() - start)

class Solution:
    def minimumLength(self, s: str) -> int:
        result = 0
        for i in range(0, 26):
            tmp = s.count(chr(ord('a') + i))
            if tmp % 2 == 1:
                result += 1
            elif tmp != 0:
                result += 2
        return result
        

if __name__ == '__main__':
    sys.exit(main())