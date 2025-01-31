using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int LargestIsland(int[][] grid)
        {
            int n = grid.Length;
            var zeros = new List<int[]>();
            int result = 0;
            int grup = 2;
            var grups = new Dictionary<int, int>();

            int dfs(int r, int c)
            {
                if (0 <= r && r < n && 0 <= c && c < n && grid[r][c] == 1)
                {
                    grid[r][c] = grup;
                    return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1);
                }
                return 0;
            }

            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++) {
                    if (grid[i][j] == 0)
                    {
                        zeros.Add([i,j]);
                    }
                    else if (grid[i][j] == 1)
                    {
                        int tmp = dfs(i, j);
                        if (tmp > result)
                            result = tmp;
                        grups[grup] = tmp;
                        grup++;
                    }
                }
            }
            if (result == 0)
                return 1;

            List<(int, int)> directions = new List<(int, int)> { (1, 0), (-1, 0), (0, 1), (0, -1) };


            foreach (var zero in zeros)
            {
                int tmp = 1;
                var visited = new List<int>();

                foreach (var dir in directions)
                {
                    int r = zero[0] + dir.Item1;
                    int c = zero[1] + dir.Item2;
                    if (0 <= r && r < n && 0 <= c && c < n && grid[r][c] != 0)
                    {
                        if (!visited.Contains(grid[r][c]))
                        {
                            visited.Add(grid[r][c]);
                            tmp += grups[grid[r][c]];
                        }
                    }
                }
                if (tmp > result)
                    result = tmp;
            }
            return result;
        }
    }
}
