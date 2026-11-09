from typing import Counter, List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        result = 0
        tmp = Counter(answers)
        for v in tmp.keys():
            result += (v + 1) * ((tmp[v] + v) // (v + 1))
        return result
