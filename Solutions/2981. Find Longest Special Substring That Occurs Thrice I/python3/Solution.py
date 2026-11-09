from collections import defaultdict
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.maximumLength("aaaa"))
    print(time.time() - start)

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        l, r = 1, n

        if not self.helper(s, n, l):
            return -1

        while l + 1 < r:
            mid = (l + r) // 2
            if self.helper(s, n, mid):
                l = mid
            else:
                r = mid

        return l

    def helper(self, s: str, n: int, x: int) -> bool:
        cnt = defaultdict(int)
        p = 0

        for i in range(n):
            while s[p] != s[i]:
                p += 1
            if i - p + 1 >= x:
                cnt[s[i]] += 1
            if cnt[s[i]] > 2:
                return True

        return False
        
        

if __name__ == '__main__':
    sys.exit(main())