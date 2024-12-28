import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.strStr("sadbutsad", "sad"))
    print(time.time() - start)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(0, len(haystack) - n+1):
            if haystack[i:n+i] == needle:
                return i
        return -1
        
        

if __name__ == '__main__':
    sys.exit(main())