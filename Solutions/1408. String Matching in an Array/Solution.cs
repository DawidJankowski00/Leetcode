using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public IList<string> StringMatching(string[] words)
        {
            string st = string.Join(" ", words);
            List<string> result = new List<string>();
            foreach (string v in words)
            {
                if (words.Any(w => w != v && w.Contains(v)))
                {
                    result.Add(v);
                }
            }
            return result;
        }
    }
}
