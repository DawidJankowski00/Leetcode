using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int ClosedIsland(int[][] grid) {
            int m = grid.Length;
            int n = grid[0].Length;

            int[,] dirs = new int[4, 2] { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };
            
            void dfs(int i, int j)
            {
                if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == 1)
                {
                    return;
                }
                grid[i][j] = 1;
                for (int d = 0; d < 4; d++)
                {
                    int ni = i + dirs[d, 0];
                    int nj = j + dirs[d, 1];
                    dfs(ni, nj);
                }
                return;
            }

            for (int i = 0; i < m; i++)
            {
                if (grid[i][0] == 0)
                {
                    dfs(i, 0);
                }
                if (grid[i][n - 1] == 0)
                {
                    dfs(i, n - 1);
                }
                
            }

            for (int j = 0; j < n; j++)
            {
                if (grid[0][j] == 0)
                {
                    dfs(0, j);
                }
                if (grid[m - 1][j] == 0)
                {
                    dfs(m - 1, j);
                }

            }

            int result = 0;
            for (int i = 1; i < m - 1; i++)
            {
                for (int j = 1; j < n - 1; j++)
                {
                    if (grid[i][j] == 0)
                    {
                        result++;
                        dfs(i, j);
                    }
                }
            }
            return result;
        }
    }
}
