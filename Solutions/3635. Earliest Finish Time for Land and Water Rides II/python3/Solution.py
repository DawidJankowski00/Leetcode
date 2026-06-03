class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        result = inf
        minL = inf
        minW = inf
        n = len(landStartTime)
        m = len(waterStartTime)

        for i in range(n):
            minL = min(minL, landStartTime[i] + landDuration[i])
        
        for i in range(m):
            minW = min(minW, waterStartTime[i] + waterDuration[i])
            result = min(result, max(minL, waterStartTime[i]) + waterDuration[i])

        for i in range(n):
            result = min(result, max(minW, landStartTime[i]) + landDuration[i])

        return result
