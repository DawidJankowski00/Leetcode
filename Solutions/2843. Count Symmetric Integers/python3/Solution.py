from typing import List

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        for i in range(low, high+1):
            tmp = str(i)
            n = len(tmp)
            if n % 2 == 1:
                continue
            a = 0
            b = 0
            n = n//2
            for j in range(0, n):
                a += int(tmp[j])
                b += int(tmp[j+n])
            if a == b:
                result += 1
        return result
