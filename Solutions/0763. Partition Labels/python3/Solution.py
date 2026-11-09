from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        htab = {}
        for i, v in enumerate(s):
            htab[v] = i
        result = []
        tmp_max = 0
        l = 0
        for i in range(len(s)):
            tmp_max = max(htab[s[i]], tmp_max)
            if i == tmp_max:
                result.append(i-l+1)
                l = i+1
        return result
