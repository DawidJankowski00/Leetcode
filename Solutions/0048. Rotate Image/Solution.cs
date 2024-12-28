using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public void Rotate(int[][] matrix)
        {
            int n = matrix.Length;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < i; j++) {
                    matrix[i][j] ^= matrix[j][i];
                    matrix[j][i] ^= matrix[i][j];
                    matrix[i][j] ^= matrix[j][i];
                }
            }

            for (int i = 0; i < n / 2; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    matrix[j][i] ^= matrix[j][n - 1 - i];
                    matrix[j][n - 1 - i] ^= matrix[j][i];
                    matrix[j][i] ^= matrix[j][n - 1 - i];
                }
            }

        }
    }
}
