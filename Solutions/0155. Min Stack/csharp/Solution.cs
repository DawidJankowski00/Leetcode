using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class MinStack
    {
        Stack<int> stack;
        Stack<int> min_elem;

        public MinStack()
        {
            stack = new Stack<int>();
            min_elem = new Stack<int>();
        }

        public void Push(int val)
        {
            stack.Push(val);
            if (min_elem.Count > 0)
            {
                val = Math.Min(min_elem.Peek(), val);
            }
            min_elem.Push(val);
        }

        public void Pop()
        {
            stack.Pop();
            min_elem.Pop();
        }

        public int Top()
        {
            return stack.Peek();
        }

        public int GetMin()
        {
            return min_elem.Peek();
        }
    }
}
