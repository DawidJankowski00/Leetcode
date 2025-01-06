import sys
import time
from typing import List
from collections import deque
def main():
    sol = Solution()
    start = time.time()
    print(sol.calculate("1 + 1"))
    print(time.time() - start)

class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        curr = 0
        result = 0
        sign = 1
        stack.appendleft(sign)
        for v in s:
            if v.isdigit():
                curr = curr * 10 + int(v)
            elif v == '(':
                stack.appendleft(sign)
            elif v == ')':
                stack.popleft()
            elif v == '+':
                result += sign * curr
                sign = 1 * stack[0]
                curr = 0
            elif v == '-':
                result += sign * curr
                sign = -1 * stack[0]
                curr = 0
        return result + sign * curr
            

if __name__ == '__main__':
    sys.exit(main())