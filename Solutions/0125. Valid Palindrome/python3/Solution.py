import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.isPalindrome("0P"))
    print(time.time() - start)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()
        return s == s[::-1]

if __name__ == '__main__':
    sys.exit(main())