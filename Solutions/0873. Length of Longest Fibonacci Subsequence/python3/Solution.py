from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        maxct = 0
        arrmap = set(arr)
        n = len(arr)
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                tmp = 2
                a = arr[i]
                b = arr[j]
                c = a + b
                while c in arrmap:
                    tmp += 1
                    a,b,c = b, c, c + b
                if tmp != 2:
                    maxct = max(tmp, maxct)
        return maxct
