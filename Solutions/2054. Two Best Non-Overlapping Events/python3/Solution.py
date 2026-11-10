from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        maxSum = 0
        n = len(events)
        suffixMax = [0] * n
        suffixMax[n - 1] = events[n - 1][2]
        for i in range(n - 2, -1, -1):
            suffixMax[i] = max(events[i][2], suffixMax[i + 1])
        for i in range(n):
            l = i
            r = n - 1 
            nextEventIndex = -1
            while l <= r:
                mid = (l + r) // 2
                if events[mid][0] > events[i][1]:
                    nextEventIndex = mid
                    r = mid - 1
                else:
                    l = mid + 1
            if nextEventIndex != -1:
                maxSum = max(maxSum, events[i][2] + suffixMax[nextEventIndex])
            maxSum = max(maxSum, events[i][2])
        return maxSum
