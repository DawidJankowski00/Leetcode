using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int[] MinOperations(string boxes)
        {
            int n = boxes.Length;
            int[] result = new int[n];
            int ball = 0;
            int curr = 0;

            for (int i = 0; i < n; i++)
            {
                result[i] = curr;
                if (boxes[i] == '1')
                    ball++;
                curr += ball;
            }
            ball = 0;
            curr = 0;
            for (int i = n - 1; i >= 0; i--)
            {
                result[i] += curr;
                if (boxes[i] == '1')
                    ball++;
                curr += ball;
            }
            return result;
        }
    }
}
