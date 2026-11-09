using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public IList<string> FullJustify(string[] words, int maxWidth)
        {
            List<string> result = new List<string>();
            var tmp = new List<string> { words[0] };
            int i = words[0].Length;
            bool f = true;
            foreach (string w in words)
            {
                if (f)
                {
                    f = false;
                    continue;
                }
                if (w.Length + i + 1 > maxWidth)
                {
                    int s = maxWidth - i;
                    int j = 0;
                    while (s != 0)
                    {
                        tmp[j] += " ";
                        j++;
                        if (j >= tmp.Count - 1)
                        {
                            j = 0;
                        }
                        s--;
                    }
                    result.Add(string.Join(" ", tmp));
                    i = w.Length;
                    tmp = new List<string>() { w };
                }
                else
                {
                    tmp.Add(w);
                    i += 1 + w.Length;
                }
            }
            if (tmp.Count > 0)
            {
                string text = string.Join(" ", tmp);
                result.Add(text + new string(' ', maxWidth - text.Length));
            }
            return result;

        }
    }
}
