from typing import List
from collections import deque

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
