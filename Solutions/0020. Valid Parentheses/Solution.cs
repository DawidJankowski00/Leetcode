using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool IsValid(string s)
        {
            Dictionary<char, char> op = new Dictionary<char, char>();
            op['('] = ')';
            op['{'] = '}';
            op['['] = ']';
            Stack<char> stack = new Stack<char>();
            foreach (char v in s)
            {
                if (op.ContainsKey(v)) stack.Push(v);
                else
                {
                    if (stack.Count == 0) return false;
                    else
                    {
                        if (op[stack.Pop()] != v) return false;
                    }
                }
            }
            return stack.Count == 0;
        }
    }
}
