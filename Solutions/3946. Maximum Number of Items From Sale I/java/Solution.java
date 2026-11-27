class Solution {
    public int maximumSaleItems(int[][] items, int budget) {
        int n = items.length;
        int[] frees = new int[n];

        for (int i = 0; i < n; i++) {
            int fi = items[i][0];
            int cnt = 0;
            for (int j = 0; j < n; j++) {
                if (i != j && items[j][0] % fi == 0) {
                    cnt++;
                }
            }
            frees[i] = cnt;
        }

        int[] dp = new int[budget + 1];

        for (int i = 0; i < n; i++) {
            int price = items[i][1];
            int free = frees[i];
            if (price > budget) {
                continue;
            }

            for (int b = budget; b >= price; b--) {
                if (dp[b - price] + 1 + free > dp[b]) {
                    dp[b] = dp[b - price] + 1 + free;
                }
            }

            for (int b = price; b <= budget; b++) {
                if (dp[b - price] + 1 > dp[b]) {
                    dp[b] = dp[b - price] + 1;
                }
            }
        }

        return dp[budget];
    }
}