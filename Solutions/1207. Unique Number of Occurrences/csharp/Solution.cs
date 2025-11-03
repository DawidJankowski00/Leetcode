using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public bool UniqueOccurrences(int[] arr) {
            Dictionary<int, int> myset = new Dictionary<int, int>();
            foreach (int v in arr)
            {
                if (myset.ContainsKey(v)) myset[v]++;
                else myset[v] = 1;
            }
            return myset.Count == new HashSet<int>(myset.Values).Count;
        }
    }
}
