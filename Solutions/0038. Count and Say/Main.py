import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.countAndSay(4))
    print(time.time() - start)

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        tmp = self.countAndSay(n-1)
        new = ""
        last = tmp[0]
        ct = 1
        for i in range(1, len(tmp)):
            if tmp[i] == last:
                ct += 1
            else:
                new += str(ct) + last
                ct = 1
                last = tmp[i]
        new += str(ct) + last
        return new
        

if __name__ == '__main__':
    sys.exit(main())