from collections import Counter, defaultdict
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))
    print(time.time() - start)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = Counter(t)
        result = ""
        l = 0
        r = 0
        n = len(s)
        m = len(dic.keys())
        status = True
        while r < n:
            if status:
                if s[r] in dic:
                    dic[s[r]] -= 1
                    if dic[s[r]] == 0:
                        m -= 1
                    if m == 0:
                        w = s[l:r+1]
                        if result == "" or len(result) > len(w):
                            result = w
                        status = False
                    else:
                        r += 1
                else:
                    r += 1
            else:
                if s[l] in dic:
                    dic[s[l]] += 1
                    if dic[s[l]] > 0:
                        m += 1
                        r += 1
                        l += 1
                        status = True
                        continue
                w = s[l+1:r+1]
                if len(result) > len(w):
                    result = w
                l += 1
        return result
        

if __name__ == '__main__':
    sys.exit(main())