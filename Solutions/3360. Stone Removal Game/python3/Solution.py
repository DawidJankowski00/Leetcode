class Solution:
    def canAliceWin(self, n: int) -> bool:
        result = False
        for i in range(10, 1, -2):
            n = n - i
            if n >= 0:
                result = True
            else:
                result = False
                break
            n = n - (i - 1)
            if n >= 0:
                result = False
            else:
                break
        return result