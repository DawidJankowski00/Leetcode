from typing import List

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        result = num1
        ones1 = bin(num1).count('1')
        ones2 = bin(num2).count('1')
        for i in range(0, 32):
            if ones1 > ones2 and (num1 & (1 << i)):
                result ^= 1 << i
                ones1 -= 1
            if ones1 < ones2 and not (num1 & (1 << i)):
                result ^= 1 << i
                ones1 += 1
        return result
