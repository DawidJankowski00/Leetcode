using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int[][] MergeArrays(int[][] nums1, int[][] nums2)
        {
            var tab = new Dictionary<int, int>();
            foreach (var v in nums1)
            {
                tab[v[0]] = v[1];
            }
            foreach (var v in nums2)
            {
                if (tab.ContainsKey(v[0]))
                    tab[v[0]] += v[1];
                else
                    tab[v[0]] = v[1];
            }
            List<int[]> result = new List<int[]>();
            var keys = tab.Keys.ToList();
            keys.Sort();
            foreach (int i in keys)
            {
                result.Add(new int[] { i, tab[i] });
            }
            return result.ToArray();
        }
    }
}
