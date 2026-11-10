from collections import defaultdict

class Solution:
    def clearDigits(self, s: str) -> str:
        result = []
        for c in s:
            if c.isalpha():
                result.append(c)
            else:
                result.pop()
        return "".join(result)
