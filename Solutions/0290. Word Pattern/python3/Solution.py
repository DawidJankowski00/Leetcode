from typing import List

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic_s = {}
        dic_t = {}
        s = s.split()
        if len(s) != len(pattern):
            return False
        for i, v in enumerate(s):
            if v not in dic_s:
                dic_s[v] = i
            if pattern[i] not in dic_t:
                dic_t[pattern[i]] = i
            if dic_s[v] != dic_t[pattern[i]]:
                return False
        return True
