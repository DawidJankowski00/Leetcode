from collections import deque
from typing import List

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
