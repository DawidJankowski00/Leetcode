import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.areAlmostEqual("bank","kanb"))
    print(time.time() - start)

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1_char = ""
        s2_char = ""
        diff_chars_count = 0
        for i in range(0,n):
            if s1[i] != s2[i] and diff_chars_count == 0:
                s1_char = s1[i]
                s2_char = s2[i]
                diff_chars_count = 1
            elif s1[i] != s2[i]:
                diff_chars_count += 1
                if diff_chars_count > 2:
                    return False
                if s1[i] == s2_char and s2[i] == s1_char:
                    continue
                return False
        if diff_chars_count == 1:
            return False
        return True

        

if __name__ == '__main__':
    sys.exit(main())