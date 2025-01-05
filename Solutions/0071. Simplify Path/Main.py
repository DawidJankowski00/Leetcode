from collections import deque
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.simplifyPath("/a/./b/../../c/"))
    print(time.time() - start)

class Solution:
    def simplifyPath(self, path: str) -> str:
        tmp = path.split('/')
        stack = deque()
        for v in tmp:
            if v == "." or v == "":
                continue
            if v == "..":
                if len(stack) > 0:
                    stack.popleft()
            else:
                stack.appendleft(v)
        stack.reverse()
        return "/" + "/".join(stack)
        

if __name__ == '__main__':
    sys.exit(main())