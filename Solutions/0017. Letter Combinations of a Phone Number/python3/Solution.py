from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        t = [
            [],
            [],
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z']
            ]
        result = []

        def backTracking(curr, next):
            if len(next) == 0:
                result.append(curr)
            else:
                for v in t[int(next[0])]:
                    backTracking(curr + v, next[1:])

        result = []
        backTracking("", digits)
        return result
