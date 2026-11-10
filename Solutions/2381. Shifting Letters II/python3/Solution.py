from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift = [0] * (n+1)
        for v in shifts:
            l = 1
            r = -1
            if v[2] == 0:
                l = -1
                r = 1
            shift[v[0]] += l
            shift[v[1]+1] += r
        curr = 0
        s = list(s)
        for i in range(0, n):
            curr += shift[i]
            s[i] = chr(ord('a') + ((ord(s[i]) - ord('a') + curr) % 26))
        return "".join(s)
