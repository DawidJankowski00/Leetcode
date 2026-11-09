from typing import List
from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        for i, v in enumerate(s):
            if v not in dic_s:
                dic_s[v] = i
            if t[i] not in dic_t:
                dic_t[t[i]] = i
            if dic_s[v] != dic_t[t[i]]:
                return False
        return True
