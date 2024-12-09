using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public string MinWindow(string s, string t)
        {
            Dictionary<char, int> dict = new Dictionary<char, int>();
            foreach (char key in t)
            {
                if (dict.ContainsKey(key))
                {
                    dict[key]++;
                }
                else
                {
                    dict.Add(key, 1);
                }
            }
            int start = 0;
            int minLen = int.MaxValue;
            int l = 0;
            int r = 0;
            int m = dict.Count;
            bool status = true;
            while (r < s.Length)
            {
                // Włącz znak `s[r]` do aktualnego okna
                if (dict.ContainsKey(s[r]))
                {
                    dict[s[r]]--;
                    if (dict[s[r]] == 0)
                        m--;
                }

                // Gdy wszystkie znaki są w oknie
                while (m == 0)
                {
                    // Aktualizuj minimalne okno
                    if (r - l + 1 < minLen)
                    {
                        minLen = r - l + 1;
                        start = l;
                    }

                    // Usuń `s[l]` z okna
                    if (dict.ContainsKey(s[l]))
                    {
                        dict[s[l]]++;
                        if (dict[s[l]] > 0)
                            m++;
                    }
                    l++;
                }

                // Przesuń wskaźnik prawy
                r++;
            }

            return minLen == int.MaxValue ? "" : s.Substring(start, minLen);
        }
    }
}
