using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int EqualPairs(int[][] grid) {
            int result = 0;
            int n = grid.Length;
            Dictionary<string, int> matrix_dict = new Dictionary<string, int>();
            for (int i = 0; i < n; i++)
            {
                List<int> tmp = new List<int>();
                for (int j = 0; j < n; j++) tmp.Add(grid[i][j]);
                string key = string.Join(",", tmp);
                if (matrix_dict.ContainsKey(key)) matrix_dict[key]++;
                else matrix_dict[key] = 1;
            }

            for (int i = 0; i < n; i++)
            {
                List<int> tmp = new List<int>();
                for (int j = 0; j < n; j++) tmp.Add(grid[j][i]);
                string key = string.Join(",", tmp);
                if (matrix_dict.ContainsKey(key)) result += matrix_dict[key];
            }
            return result;
        }
    }
}
