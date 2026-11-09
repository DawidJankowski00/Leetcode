using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public IList<int> SpiralOrder(int[][] matrix)
        {
            if (matrix.Length == 0)
            {
                return new List<int>();
            }
            List<int> result = new List<int>();
            int row_begin = 0;
            int row_end = matrix.Length - 1;
            int col_begin = 0;
            int col_end = matrix[0].Length - 1;
            while (row_begin <= row_end && col_begin <= col_end)
            {
                for (int i = col_begin; i < col_end + 1; i++) result.Add(matrix[row_begin][i]);
                row_begin++;
                for (int i = row_begin; i < row_end + 1; i++) result.Add(matrix[i][col_end]);
                col_end--;
                if (row_begin <= row_end)
                {
                    for (int i = col_end; i > col_begin - 1; i--) result.Add(matrix[row_end][i]);
                    row_end--;
                }
                if (col_begin <= col_end)
                {
                    for (int i = row_end; i > row_begin - 1; i--) result.Add(matrix[i][col_begin]);
                    col_begin++;
                }
            }
            return result;
        }
    }
}
