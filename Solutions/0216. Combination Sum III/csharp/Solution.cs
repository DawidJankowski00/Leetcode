using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public IList<IList<int>> CombinationSum3(int k, int n) {
            List<IList<int>> result = new List<IList<int>>();
            void Backtrack(int curr_k, int curr_n, int start, List<int> path) {
                if (curr_k == 0 && curr_n == 0) {
                    result.Add(new List<int>(path));
                    return;
                }
                if (curr_k < 0 || curr_n < 0) {
                    return;
                }
                for (int i = start; i <= 9; i++) {
                    path.Add(i);
                    Backtrack(curr_k - 1, curr_n - i, i + 1, path);
                    path.RemoveAt(path.Count - 1);
                }
            }
            Backtrack(k, n, 1, new List<int>());
            return result;
        }
    }
}
