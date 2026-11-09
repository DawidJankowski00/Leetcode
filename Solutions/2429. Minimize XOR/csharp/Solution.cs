using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    using System;

public class Solution
{
    public int MinimizeXor(int num1, int num2)
    {
        int result = num1;
        int ones1 = CountOnes(num1);
        int ones2 = CountOnes(num2);

        for (int i = 0; i < 32; i++)
        {
            if (ones1 > ones2 && (num1 & (1 << i)) != 0)
            {
                result ^= (1 << i);
                ones1--;
            }
            if (ones1 < ones2 && (num1 & (1 << i)) == 0)
            {
                result ^= (1 << i);
                ones1++;
            }
        }

        return result;
    }

    private int CountOnes(int num)
    {
        int count = 0;
        while (num > 0)
        {
            count += (num & 1);
            num >>= 1;
        }
        return count;
    }
}

}
