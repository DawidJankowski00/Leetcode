class Solution:
    def numSteps(self, s: str) -> int:
        result = 0
        carry = 0
        n = len(s)
        for i in range(n-1, 0, -1):
            if int(s[i]) + carry == 1:
                result += 2
                carry = 1
            else:
                result += 1

        return result + carry