using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int FindMaxFish(int[][] grid)
        {
            int m = grid.Length;
            int n = grid[0].Length;
            int result = 0;

            int dfs(int r, int c)
            {
                if(0 <= r && r < m && 0 <= c && c < n && grid[r][c] != 0)
                {
                    int res = grid[r][c];
                    grid[r][c] = 0;
                    return res + dfs(r+1, c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1);
                }
                return 0;
            }

            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++)
                {
                    if (grid[i][j] != 0)
                    {
                        result = Math.Max(result, dfs(i, j));
                    }
                }
            }
            return result;
        }
    }
}
