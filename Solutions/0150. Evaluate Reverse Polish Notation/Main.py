from collections import deque
import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    print(time.time() - start)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for v in tokens:
            if v == '+':
                stack.appendleft(stack.popleft() + stack.popleft())
            elif v == '-':
                a = stack.popleft()
                b = stack.popleft()
                stack.appendleft(b - a)
            elif v == '*':
                stack.appendleft(stack.popleft() * stack.popleft())
            elif v == '/':
                a = stack.popleft()
                b = stack.popleft()
                stack.appendleft(int(b / a))
            else:
                stack.appendleft(int(v))
        return stack.popleft()

if __name__ == '__main__':
    sys.exit(main())