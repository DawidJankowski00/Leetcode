import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.isSubsequence("abc", "ahbgdc"))
    print(time.time() - start)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        i = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

if __name__ == '__main__':
    sys.exit(main())