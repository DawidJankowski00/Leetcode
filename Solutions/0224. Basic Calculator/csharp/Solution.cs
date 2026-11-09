using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int Calculate(string s)
        {
            Stack<int> stack = new Stack<int>();
            int curr = 0;
            int result = 0;
            int sign = 1;
            stack.Push(sign);
            foreach (char v in s)
            {
                if (int.TryParse(v.ToString(), out int c))
                {
                    curr = curr * 10 + c;
                }
                else if (v == '(')
                    stack.Push(sign);
                else if (v == ')')
                    stack.Pop();
                else if (v == '+')
                {
                    result += sign * curr;
                    sign = 1 * stack.Peek();
                    curr = 0;
                }
                else if (v == '-')
                {
                    result += sign * curr;
                    sign = -1 * stack.Peek();
                    curr = 0;
                }
            }
            return result + sign * curr;
        }
    }
}
