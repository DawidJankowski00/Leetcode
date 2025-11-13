using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int FindCircleNum(int[][] isConnected) {
            HashSet<int> visited = new();
            HashSet<int> to_visit = new();
            int result = 0;
            int n = isConnected.Length;

            for (int i = 0; i < n; i++)
            {
                if (visited.Contains(i)) continue;
                visited.Add(i);
                result++;
                to_visit.Add(i);
                while (to_visit.Count > 0)
                {
                    int k = to_visit.First();
                    visited.Add(k);
                    to_visit.Remove(k);
                    for (int j = 0; j < n; j++) if (isConnected[k][j] == 1 && !visited.Contains(j) && !to_visit.Contains(j)) to_visit.Add(j);
                }
            }
            return result;
        }
    }
}
