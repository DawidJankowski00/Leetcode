import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.reverseWords(" "))
    print(time.time() - start)

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
        

if __name__ == '__main__':
    sys.exit(main())