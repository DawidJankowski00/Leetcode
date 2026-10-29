using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int MinCost(int[][] grid) {
            int m = grid.Length;
            int n = grid[0].Length;

            HashSet<int>[] dp = new HashSet<int>[n];
            for (int j = 0; j < n; j++) {
                dp[j] = new HashSet<int>();
            }

            dp[0].Add(grid[0][0]);

            for (int j = 1; j < n; j++) {
                int val = grid[0][j];
                foreach (int x in dp[j - 1]) {
                    dp[j].Add(x ^ val);
                }
            }

            for (int i = 1; i < m; i++) {
                HashSet<int> nextDp0 = new HashSet<int>();
                int firstVal = grid[i][0];
                foreach (int x in dp[0]) {
                    nextDp0.Add(x ^ firstVal);
                }
                dp[0] = nextDp0;

                for (int j = 1; j < n; j++) {
                    int val = grid[i][j];
                    HashSet<int> nextCell = new HashSet<int>();

                    foreach (int x in dp[j]) {
                        nextCell.Add(x ^ val);
                    }
                    foreach (int x in dp[j - 1]) {
                        nextCell.Add(x ^ val);
                    }

                    dp[j] = nextCell;
                }
            }

            return dp[n - 1].Min();
        }
    }
}
