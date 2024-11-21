import sys
from typing import List
def main():
    sol = Solution()
    print(sol.makeFancyString("aaabaaaa"))

class Solution:
    def makeFancyString(self, s: str) -> str:
        k = 0
        last = ''
        newstring = ""
        for i in range(0, len(s)):
            if last == s[i]:
                k += 1
            else:
                k = 0
                last = s[i]
            if k < 2:
                newstring += s[i]
        return newstring

        

if __name__ == '__main__':
    sys.exit(main())