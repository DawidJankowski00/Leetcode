using System;
using System.Collections.Generic;
using System.Data.Common;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int FirstCompleteIndex(int[] arr, int[][] mat)
        {
            int n = mat.Length;
            int m = mat[0].Length;
            int[] cols = new int[n];
            int[] rows = new int[m];
            var cordscol = new int[m*n+1];
            var cordsrow = new int[m * n + 1];
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    cordscol[mat[i][j]] = i;
                    cordsrow[mat[i][j]] = j;
                }
            }

            for (int i = 0;i < n*m; i++)
            {
                int c = cordscol[arr[i]];
                int r = cordsrow[arr[i]];
                cols[c]++;
                if (cols[c] == m)
                    return i;
                rows[r]++;
                if (rows[r] == n)
                    return i;
            }
            return -1;
        }
    }
}
