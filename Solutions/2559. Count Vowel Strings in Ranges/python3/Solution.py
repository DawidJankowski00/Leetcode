from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        vovels = set(['a', 'e', 'i', 'o', 'u'])
        n = len(words)
        pre_sum = [0]
        for i in range(0, n):
            if words[i][0] in vovels and words[i][-1] in vovels:
                pre_sum.append(pre_sum[i] + 1)
            else:
                pre_sum.append(pre_sum[i])
        for x, y in queries:
            result.append(pre_sum[y+1]- pre_sum[x])
        return result
