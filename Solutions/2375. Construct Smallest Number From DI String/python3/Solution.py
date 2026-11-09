import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.smallestNumber("IIIDIDDD"))
    print(time.time() - start)

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        result = ""
        st = []

        for i in range(0, n+1):
            st.append(i + 1)
            if i == n or pattern[i] == 'I':
                while st:
                    result += str(st.pop())
        return result
        

if __name__ == '__main__':
    sys.exit(main())