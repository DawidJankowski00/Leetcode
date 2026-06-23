from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = Counter(text)
        return min(freq["b"], freq["a"], freq["n"], freq["l"] //2, freq["o"] //2)