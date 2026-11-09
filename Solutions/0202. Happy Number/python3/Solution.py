from collections import defaultdict
from typing import List

class Solution:
    def isHappy(self, n: int) -> bool:
        dic  = defaultdict(int)
        while n not in dic:
            if n == 1:
                return True
            dic[n] = 0
            tmp = 0
            while n != 0:
                tmp += (n%10) ** 2
                n -= n%10
                n = n // 10
            n = tmp
        return False
