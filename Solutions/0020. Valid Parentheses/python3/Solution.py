from collections import defaultdict, deque
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.isValid("()"))
    print(time.time() - start)

class Solution:
    def isValid(self, s: str) -> bool:
        op = defaultdict(chr)
        op['('] = ')'
        op['{'] = '}'
        op['['] = ']'
        stack = deque()
        for v in s:
            if v in op:
                stack.appendleft(v)
            else:
                if stack:
                    c = stack.popleft()
                    if op[c] != v:
                        return False
                else:
                    return False
        if stack:
            return False
        return True

if __name__ == '__main__':
    sys.exit(main())