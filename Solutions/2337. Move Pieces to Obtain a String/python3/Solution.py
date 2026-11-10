from typing import List

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i = 0
        j = 0
        n = len(start)
        start += "@"
        target += "@"
        while i < n or j < n:
            while i < n and start[i] == "_":
                i += 1
            while j < n and target[j] == "_":
                j += 1
            if start[i] != target[j]:
                return False
            if start[i] == "L" and i<j:
                return False
            if start[i] == "R" and i>j:
                return False
            j += 1
            i += 1
        return True
