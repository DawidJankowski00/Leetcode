using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public IList<bool> KidsWithCandies(int[] candies, int extraCandies) {
            int m = 0;
            foreach (int v in candies) m = Math.Max(m, v);
            List<bool> result = new();
            foreach (int v in candies) result.Add(m <= v + extraCandies);
            return result;
        }
    }
}
