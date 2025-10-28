from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        l1 = 0
        l2 = 0
        curr = 0
        n = len(chars)
        while l2 < n:
            while l2 < n and chars[l2] == chars[curr]:
                l2 += 1
            ct = l2 - curr
            chars[l1] = chars[curr]
            l1 += 1
            if ct > 1:
                tmp = str(ct)
                for v in tmp:
                    chars[l1] = v
                    l1 += 1
            curr = l2
        return l1