class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        j = 0
        result = 0
        for i in range(len(cost) - 1, -1, -1):
            if j == 2:
                j = 0
                continue
            j += 1
            result += cost[i]
        return result