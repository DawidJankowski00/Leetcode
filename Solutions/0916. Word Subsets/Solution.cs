using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public IList<string> WordSubsets(string[] words1, string[] words2)
        {
            Dictionary<char, int> neded = new Dictionary<char, int>();
            foreach (string v in words2)
            {
                var tmp = new Dictionary<char, int>();
                foreach (char c in v)
                {
                    if (tmp.ContainsKey(c))
                        tmp[c]++;
                    else
                        tmp[c] = 1;
                }
                foreach (char c in tmp.Keys)
                {
                    if (!neded.ContainsKey(c))
                        neded[c] = tmp[c];
                    else
                    {
                        if (neded[c] < tmp[c])
                            neded[c] = tmp[c];
                    }
                }
            }
            List<string> result = new List<string>();
            foreach (string v in words1)
            {
                var tmp = new Dictionary<char, int>();
                foreach (char c in v)
                {
                    if (tmp.ContainsKey(c))
                        tmp[c]++;
                    else
                        tmp[c] = 1;
                }
                bool test = true;
                foreach (char c in neded.Keys)
                {
                    if (tmp.ContainsKey(c))
                    {
                        if (tmp[c] >= neded[c])
                            continue;
                    }
                    test = false;
                    break;
                }
                if (test)
                    result.Add(v);
            }
            return result;
        }
    }
}
