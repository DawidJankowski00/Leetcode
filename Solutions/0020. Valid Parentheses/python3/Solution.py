from collections import defaultdict, deque
from typing import List

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
