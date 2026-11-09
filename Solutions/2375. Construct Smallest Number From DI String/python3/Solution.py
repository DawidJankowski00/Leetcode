from typing import List

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        result = ""
        st = []

        for i in range(0, n+1):
            st.append(i + 1)
            if i == n or pattern[i] == 'I':
                while st:
                    result += str(st.pop())
        return result
