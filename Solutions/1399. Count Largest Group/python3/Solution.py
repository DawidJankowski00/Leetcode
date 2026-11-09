from collections import defaultdict
from typing import List

class Solution:
    def countLargestGroup(self, n: int) -> int:
        ct = defaultdict(int)
        for i in range(1, n+1):
            tmp = str(i)
            tmp_ct = 0
            for v in tmp:
                tmp_ct += int(v)
            ct[tmp_ct] += 1
        max_result = max(ct.values())
        result = 0
        for v in ct.values():
            if max_result == v:
                result += 1
        return result
