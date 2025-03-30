using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public IList<int> PartitionLabels(string s)
        {
            var htab = new Dictionary<char, int>();
            for (int i = 0; i < s.Length; i++)
            {
                htab[s[i]] = i;
            }
            var result = new List<int>();
            int l = 0;
            int tmp_max = 0;
            for (int i = 0; i< s.Length; i++)
            {
                tmp_max = Math.Max(tmp_max, htab[s[i]]);
                if (i == tmp_max)
                {
                    result.Add(i-l + 1);
                    l = i + 1;
                }
            }
            return result;
        }
    }
}
