from collections import deque
from typing import List

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
