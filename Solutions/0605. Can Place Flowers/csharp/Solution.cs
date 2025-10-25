using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public bool CanPlaceFlowers(int[] flowerbed, int n) {
            int tmp = 0;
            int k = flowerbed.Length;
            if (k < 3)
            {
                foreach (int v in flowerbed) if (v == 1) return n <= 0;
                return n <= 1;
            }
            if (flowerbed[0] == 0 && flowerbed[1] == 0)
            {
                flowerbed[0] = 1;
                tmp++;
            }
            for (int i = 1; i < k - 1; i++)
            {
                if (flowerbed[i - 1] == 0 && flowerbed[i] == 0 && flowerbed[i + 1] == 0)
                {
                    flowerbed[i] = 1;
                    tmp++;
                }
            }
            if (flowerbed[k - 2] == 0 && flowerbed[k - 1] == 0)
            {
                tmp++;
            }
            return tmp >= n;
            
        }
    }
}
