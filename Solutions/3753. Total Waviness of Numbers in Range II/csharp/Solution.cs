using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        private static readonly List<int> patterns = new List<int>();

        static Solution()
        {
            for (int i = 0; i < 1000; i++)
            {
                int r = i % 10;
                int m = (i / 10) % 10;
                int l = (i / 100) % 10;

                if ((m > Math.Max(l, r)) || (m < Math.Min(l, r)))
                {
                    patterns.Add(i);
                }
            }
        }


        public long TotalWaviness(long num1, long num2)
        {
            return WaveCount(num2) - WaveCount(num1 - 1);
        }

        public long WaveCount(long num)
        {
            if (num < 100)
            {
                return 0;
            }

            long sum = 0; 
            foreach (int p in patterns)
            {
                sum += CountWays(num, p);
            }
            return sum;
        }

        public long CountWays(long num, int pattern)
        {
            string s = num.ToString();
            int n = s.Length;
            long result = 0; 
            
            int t = (pattern < 100) ? 1 : 0; 

            for (int i = 0; i < n - 2; i++)
            {
                string leftStr = s.Substring(0, i);
                string midStr = s.Substring(i, 3);
                string rightStr = s.Substring(i + 3);

                long l = string.IsNullOrEmpty(leftStr) ? 0 : long.Parse(leftStr); 
                int m = int.Parse(midStr);
                long r = string.IsNullOrEmpty(rightStr) ? 0 : long.Parse(rightStr); 

                long mult = (long)Math.Pow(10, n - i - 3); 
                long tmp = 0; 

                if (m > pattern)
                {
                    tmp = l - t + 1;
                }
                else if (m == pattern)
                {
                    tmp = Math.Max(0, l - t);
                    result += r + 1;
                }
                else
                {
                    tmp = Math.Max(0, l - t);
                }

                result += mult * tmp;
            }

            return result;
        }
    }
}
