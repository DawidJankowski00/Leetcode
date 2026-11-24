class Solution:
    def checkString(self, s: str) -> bool:
        b = False
        for v in s:
            if v == 'b':
                b = True
            else:
                if b == True:
                    return False
        return True