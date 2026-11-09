using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int EvalRPN(string[] tokens)
        {
            Stack<int> stack = new Stack<int>();
            foreach (string v in tokens)
            {
                if (v == "+")
                    stack.Push(stack.Pop() + stack.Pop());
                else if (v == "-")
                {
                    int a = stack.Pop();
                    int b = stack.Pop();
                    stack.Push(b - a);
                }
                else if (v == "*")
                    stack.Push(stack.Pop() * stack.Pop());
                else if (v == "/")
                {
                    int a = stack.Pop();
                    int b = stack.Pop();
                    stack.Push(b / a);
                }
                else stack.Push(int.Parse(v));
            }
            return stack.Pop();
        }
    }
}
