using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int CountServers(int[][] grid)
        {
            int m = grid.Length;
            int n = grid[0].Length;
            int result = 0;
            for (int i = 0; i < m; i++)
            {
                int curr_row = 0;
                int col = 0;
                for (int j = 0; j < n; j++)
                {
                    if (grid[i][j] == 1)
                    {
                        curr_row++;
                        col = j;
                    }
                }
                if (curr_row == 1)
                {
                    for (int k = 0; k < m; k++)
                    {
                        if (k != i && grid[k][col] == 1)
                        {
                            result++;
                            break;
                        }
                    }
                }
                else
                    result += curr_row;
            }
            return result;

        }
    }
}
