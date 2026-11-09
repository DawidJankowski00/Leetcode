using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public string ClearDigits(string s)
        {
            StringBuilder result = new StringBuilder();

            foreach (char c in s)
            {
                if (char.IsLetter(c))
                {
                    result.Append(c);
                }
                else if (result.Length > 0)
                {
                    result.Remove(result.Length - 1, 1);
                }
            }

            return result.ToString();
        }
    }
}
