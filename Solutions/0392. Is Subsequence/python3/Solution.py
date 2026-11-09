class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sc = 0
        tc = 0
        sn = len(s)
        tn = len(t)
        while sc < sn and tc < tn:
            if s[sc] == t[tc]:
                sc+=1
            tc+=1
        return sc == sn