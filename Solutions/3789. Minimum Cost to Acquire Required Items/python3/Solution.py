class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        result = 0
        x = min(need1, need2)

        a = x * cost1 + x * cost2
        b = x * costBoth
        result += min(a, b)
        
        y = 0
        if x == need1:
            y = need2 - need1
            if cost2 > costBoth:
                result += y * costBoth
            else:
                result += y * cost2
        else:
            y = need1 - need2
            if cost1 > costBoth:
                result += y * costBoth
            else:
                result += y * cost1
        return result