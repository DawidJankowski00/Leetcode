using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int CountServers(int[][] grid) {
            int m = grid.Length;
            int n = grid[0].Length;

            int[] row_count = new int[m];
            int[] col_count = new int[n];
            int ans = 0;

            // Zliczanie liczby serwerów w każdym wierszu i kolumnie
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (grid[i][j] == 1) {
                        row_count[i]++;
                        col_count[j]++;
                    }
                }
            }

            // Sprawdzanie, czy dany serwer może komunikować się z innym
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (grid[i][j] == 1 && (row_count[i] > 1 || col_count[j] > 1)) {
                        ans++;
                    }
                }
            }

            return ans;
        }
    }
}
