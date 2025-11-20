using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public IList<string> LetterCombinations(string digits) {
            string[] t = new string[] {
                "",                 // 0
                "",                 // 1
                "abc",              // 2
                "def",              // 3
                "ghi",              // 4
                "jkl",              // 5
                "mno",              // 6
                "pqrs",             // 7
                "tuv",              // 8
                "wxyz"              // 9
            };
            List<string> result = new List<string>();
            if (string.IsNullOrEmpty(digits))
            {
                return result;
            }
            void Backtrack(string curr, string nextDigits)
            {
                if (nextDigits.Length == 0)
                {
                    result.Add(curr);
                }
                else
                {
                    string letters = t[nextDigits[0] - '0'];
                    for (int i = 0; i < letters.Length; i++)
                    {
                        Backtrack(curr + letters[i], nextDigits.Substring(1));
                    }
                }
            }
            Backtrack("", digits);
            return result;
        }
    }
}
