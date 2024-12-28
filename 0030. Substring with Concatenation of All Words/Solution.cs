using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public IList<int> FindSubstring(string s, string[] words)
        {
            Dictionary<string, int> dic = new Dictionary<string, int>();
            foreach (string word in words)
            {
                if (dic.ContainsKey(word))
                {
                    dic[word]++;
                }
                else
                {
                    dic.Add(word, 1);
                }
            }
            int n = words[0].Length;
            int m = s.Length;
            List<int> result = new List<int>();
            for (int i = 0; i < n; i++)
            {
                int l = i;
                Dictionary<string, int> window = new Dictionary<string, int>();
                int c = 0;
                for (int j = i; j <= m -n; j += n)
                {
                    string word = s.Substring(j, n);
                    if (!dic.ContainsKey(word))
                    {
                        l = j + n;
                        window.Clear();
                        c = 0;
                        continue;
                    }
                    c++;
                    if (window.ContainsKey(word))
                    {
                        window[word]++;
                    }
                    else
                    {
                        window[word] = 1;
                    }
                    while (window[word] > dic[word])
                    {
                        string leftWord = s.Substring(l, n);
                        window[s.Substring(l, n)]--;
                        if (window[leftWord] == 0)
                        {
                            window.Remove(leftWord);
                        }
                        l += n;
                        c--;
                    }
                    if (c == words.Length)
                    {
                        result.Add(l);
                    }
                }
            }

            return result;
        }
    }
}
