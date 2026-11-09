import sys
import time
from typing import List
def main():
    sol = Solution()
    start = time.time()
    print(sol.shortestCommonSupersequence("abac","cab"))
    print(time.time() - start)

class Solution:
    def shortestCommonSupersequence(self, text1: str, text2: str) -> str:
        m, n = len(text1), len(text2)
        dp_table = [[0] * (n + 1) for _ in range(m + 1)]
        
        for idx1 in range(1, m + 1):
            for idx2 in range(1, n + 1):
                if text1[idx1-1] == text2[idx2-1]:
                    dp_table[idx1][idx2] = 1 + dp_table[idx1-1][idx2-1]
                else:
                    dp_table[idx1][idx2] = max(dp_table[idx1-1][idx2], dp_table[idx1][idx2-1])
        
        idx1, idx2 = m, n
        supersequence = []
        
        while idx1 > 0 and idx2 > 0:
            if text1[idx1-1] == text2[idx2-1]:
                supersequence.append(text1[idx1-1])
                idx1 -= 1
                idx2 -= 1
            elif dp_table[idx1-1][idx2] > dp_table[idx1][idx2-1]:
                supersequence.append(text1[idx1-1])
                idx1 -= 1
            else:
                supersequence.append(text2[idx2-1])
                idx2 -= 1
        
        while idx1 > 0:
            supersequence.append(text1[idx1-1])
            idx1 -= 1
        
        while idx2 > 0:
            supersequence.append(text2[idx2-1])
            idx2 -= 1
        
        return ''.join(supersequence[::-1])

        

if __name__ == '__main__':
    sys.exit(main())