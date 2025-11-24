from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            if cost[i+1] <= cost[i+2]:
                cost[i] += cost[i+1]
            else:
                cost[i] += cost[i + 2]
        if cost[0] <= cost[1]:
            return cost[0]
        else:
            return cost[1]