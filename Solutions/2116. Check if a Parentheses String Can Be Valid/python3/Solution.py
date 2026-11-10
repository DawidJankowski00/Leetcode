from collections import deque
from typing import List

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False 
        open_count = 0
        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == '(':
                    open_count += 1
                else:
                    open_count -= 1
            else:
                open_count += 1
            if open_count < 0:
                return False

        close_count = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '1':
                if s[i] == ')':
                    close_count += 1
                else:
                    close_count -= 1
            else:
                close_count += 1 
            if close_count < 0:
                return False

        return True
