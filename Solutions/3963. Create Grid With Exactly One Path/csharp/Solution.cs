using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public string[] CreateGrid(int m, int n) {
            string[] grid = new string[m];

            string patternRow = "." + new string('#', n - 1);
            for (int i = 0; i < m - 1; i++) 
            {
                grid[i] = patternRow;
            }
            
            grid[m - 1] = new string('.', n);

            return grid;
        }
    }
}
