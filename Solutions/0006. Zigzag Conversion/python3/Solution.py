from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = [""] * numRows
        state = True
        i = 0
        current = 0
        for i in s:
            result[current] += i
            if state:
                current += 1
            else:
                current -= 1
            if current == numRows - 1 or current == 0:
                state = not state
            
        return "".join(result)
