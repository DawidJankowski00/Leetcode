using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int CountIslands(int[][] grid, int k) {
            int m = grid.Length;
            int n = grid[0].Length;

            int[,] dirs = new int[,] { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };

            long dfs(int i, int j) {
                if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == 0) {
                    return 0;
                }

                long sum = grid[i][j];
                grid[i][j] = 0;

                for (int d = 0; d < dirs.GetLength(0); d++) {
                    int ni = i + dirs[d, 0];
                    int nj = j + dirs[d, 1];
                    sum += dfs(ni, nj);
                }

                return sum;
            }

            int result = 0;
            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (grid[i][j] != 0)
                    {
                        long totalValue = dfs(i, j);
                        if (totalValue % k == 0)
                        {
                            result++;
                        }
                    }
                }
            }
            return result;
        }
    }
}
