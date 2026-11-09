import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.removeOccurrences("daabcbaabcbc","abc"))
    print(time.time() - start)

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part,"",1)
        return s

        

if __name__ == '__main__':
    sys.exit(main())