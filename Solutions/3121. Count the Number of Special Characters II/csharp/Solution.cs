using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int NumberOfSpecialChars(string word) {
            int result = 0;
            Dictionary<char, int> first_upper = new Dictionary<char, int>();
            Dictionary<char, int> last_lower = new Dictionary<char, int>();
            for (int i = 0; i < word.Length; i++)
            {
                char v = word[i];
                if (char.IsLower(v)) last_lower[v] = i;

                else
                {
                    char lower = char.ToLower(v);
                    if (!first_upper.ContainsKey(lower)) first_upper[lower] = i;
                }
            }
            foreach (var v in last_lower.Keys) if (first_upper.ContainsKey(v) && first_upper[v] > last_lower[v]) result++;

            return result;
        }
    }
}
