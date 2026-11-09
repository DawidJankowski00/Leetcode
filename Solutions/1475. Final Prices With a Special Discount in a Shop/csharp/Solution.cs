using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int[] FinalPrices(int[] prices)
        {
            int n = prices.Length;
            for (int l = 0; l < n; l++)
            {
                int r = l + 1;
                while (r < n)
                {
                    if (prices[l] >= prices[r])
                    {
                        prices[l] -= prices[r];
                        break;
                    }
                    r++;
                }
            }
            return prices;
        }
    }
}
