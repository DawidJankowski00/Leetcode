using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public string MergeAlternately(string word1, string word2) {
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < Math.Min(word1.Length, word2.Length); i++)
            {
                result.Append(word1[i]);
                result.Append(word2[i]);
            }
            if (word1.Length > word2.Length) return result.Append(word1.Substring(word2.Length)).ToString();
            if (word2.Length > word1.Length) return result.Append(word2.Substring(word1.Length)).ToString();
            return result.ToString();
        }
    }
}
