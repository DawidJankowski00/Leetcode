from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations.reverse()
        result = 0
        for i in range(0, len(citations)):
            if i+1 <= citations[i]:
                result += 1
            else:
                break
        return(result)
