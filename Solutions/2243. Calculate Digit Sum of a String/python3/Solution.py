class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        
        result = ''
        tab = []
        while len(s) > k:
            tab.append(s[0:k])
            s = s[k:]
        tab.append(s)
        
        for v in tab:
            curr = 0
            for ch in v:
                curr += int(ch)
            result += str(curr)
            
        return self.digitSum(result, k)