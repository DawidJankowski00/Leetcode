import sys
from typing import List
def main():
    sol = Solution()
    print(sol.reverseString(["h","e","l","l","o"]))

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]


        

if __name__ == '__main__':
    sys.exit(main())