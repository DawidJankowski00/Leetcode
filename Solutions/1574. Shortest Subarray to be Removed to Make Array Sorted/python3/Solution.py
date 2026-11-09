from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        result = 0
        for i in range(1, len(arr)):
            tabs = []
            j = 0
            while(j+i < len(arr)):
                tabs.append(arr[0:j-1]+arr[j:])
                j+=1

        return result
