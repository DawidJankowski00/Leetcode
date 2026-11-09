from collections import Counter
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.isAnagram("anagram", "nagaram"))
    print(time.time() - start)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

if __name__ == '__main__':
    sys.exit(main())