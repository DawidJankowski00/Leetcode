using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public bool CloseStrings(string word1, string word2) {
            if (word1.Length != word2.Length) return false;
            var counts1 = word1.GroupBy(c => c).ToDictionary(g => g.Key, g => g.Count());
            var counts2 = word2.GroupBy(c => c).ToDictionary(g => g.Key, g => g.Count());

            var keys1 = new HashSet<char>(counts1.Keys);
            var keys2 = new HashSet<char>(counts2.Keys);
            if (!keys1.SetEquals(keys2))
            {
                return false;
            }
            var values1 = counts1.Values.OrderBy(v => v).ToList();
            var values2 = counts2.Values.OrderBy(v => v).ToList();
            return values1.SequenceEqual(values2);
        }
    }
}
