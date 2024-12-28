import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.lengthOfLastWord("Hello World"))
    print(time.time() - start)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1])

if __name__ == '__main__':
    sys.exit(main())