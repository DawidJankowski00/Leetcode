from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        t = ""
        j = 0
        m = len(spaces)
        for i, v in enumerate(s):
            if m > j:
                if i == spaces[j]:
                    j += 1
                    t += " "
            t += v
        return t
