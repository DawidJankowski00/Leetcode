import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.prefixCount(["pay","attention","practice","attend"],"at"))
    print(time.time() - start)

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        for v in words:
            if v.startswith(pref):
                result += 1
        return result

if __name__ == '__main__':
    sys.exit(main())