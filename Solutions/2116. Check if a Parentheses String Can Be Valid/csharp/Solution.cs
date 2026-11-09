using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool CanBeValid(string s, string locked)
        {
            int n = s.Length;
            if (n % 2 != 0)
                return false;
            int open_count = 0;
            for (int i = 0; i < n; i++)
            {
                if (locked[i] == '1')
                {
                    if (s[i] == '(')
                        open_count++;
                    else
                        open_count--;
                }
                else
                    open_count++;
                if (open_count < 0)
                    return false;
            }
            int close_count = 0;
            for (int i = n-1; i >= 0; i--)
            {
                if (locked[i] == '1')
                {
                    if (s[i] == ')')
                        close_count++;
                    else
                        close_count--;
                }
                else
                    close_count++;
                if (close_count < 0)
                    return false;
            }
            return true;
        }
    }
}
