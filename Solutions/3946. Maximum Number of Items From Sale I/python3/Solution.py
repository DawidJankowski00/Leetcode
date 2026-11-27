from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        frees = [0] * n

        for i in range(n):
            fi, _ = items[i]
            cnt = 0
            for j in range(n):
                if i != j:
                    fj, _ = items[j]
                    if fj % fi == 0:
                        cnt += 1
            frees[i] = cnt

        dp = [0] * (budget + 1)

        for i in range(n):
            _, price = items[i]
            free = frees[i]
            if price > budget:
                continue

            for b in range(budget, price - 1, -1):
                if dp[b - price] + 1 + free > dp[b]:
                    dp[b] = dp[b - price] + 1 + free

            for b in range(price, budget + 1):
                if dp[b - price] + 1 > dp[b]:
                    dp[b] = dp[b - price] + 1

        return dp[budget]