import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int minimumChanges(String s, int k) {
        int n = s.length();
        char[] chars = s.toCharArray();

        @SuppressWarnings("unchecked")
        List<Integer>[] divisors = new List[n + 1];
        for (int len = 2; len <= n; len++) {
            divisors[len] = new ArrayList<>();
            for (int d = 1; d < len; d++) {
                if (len % d == 0) {
                    divisors[len].add(d);
                }
            }
        }

        int[][] cost = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int len = j - i + 1;
                int minChanges = len;
                for (int d : divisors[len]) {
                    int changes = 0;
                    for (int r = 0; r < d; r++) {
                        int left = i + r;
                        int right = j - d + 1 + r;
                        while (left < right) {
                            if (chars[left] != chars[right]) {
                                changes++;
                            }
                            left += d;
                            right -= d;
                        }
                    }
                    if (changes < minChanges) {
                        minChanges = changes;
                    }
                }
                cost[i][j] = minChanges;
            }
        }

        int inf = n + 1;
        int[] dp = new int[n + 1];
        Arrays.fill(dp, inf);
        for (int i = 2; i <= n; i++) {
            dp[i] = cost[0][i - 1];
        }

        for (int p = 2; p <= k; p++) {
            int[] nextDp = new int[n + 1];
            Arrays.fill(nextDp, inf);
            for (int i = 2 * p; i <= n; i++) {
                for (int prev = 2 * (p - 1); prev <= i - 2; prev++) {
                    int candidate = dp[prev] + cost[prev][i - 1];
                    if (candidate < nextDp[i]) {
                        nextDp[i] = candidate;
                    }
                }
            }
            dp = nextDp;
        }

        return dp[n];
    }
}
