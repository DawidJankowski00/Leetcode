from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        tab = {}
        n = len(nums)
        for v in nums:
            tab[int(v,2)] = True
        i = 0
        result = ''
        while True:
            if i in tab:
                i += 1
            else:
                result = bin(i)[2:]
                break
        while len(result) != n:
            result = '0' + result
        return result
