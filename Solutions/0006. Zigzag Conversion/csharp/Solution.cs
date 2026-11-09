using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public string Convert(string s, int numRows)
        {
            if (numRows == 1)
            {
                return s;
            }
            string[] result = new string[numRows];
            bool state = true;
            int current = 0;
            foreach (char ss in s)
            {
                result[current] += ss;
                if (state)
                {
                    current++;
                }
                else
                {
                    current--;
                }
                if (current == numRows - 1 || current == 0)
                {
                    state = !state;
                }
            }
            return string.Concat(result);
        }
    }
}
