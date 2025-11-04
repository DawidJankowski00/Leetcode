using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution 
    {
        public int[] AsteroidCollision(int[] asteroids) 
        {
            Stack<int> stack = new Stack<int>();
            
            foreach (int v in asteroids)
            {
                bool alive = true; 

                while (stack.Count > 0 && stack.Peek() > 0 && v < 0)
                {
                    int topAsteroid = stack.Peek();
                    int currentMass = -v;

                    if (topAsteroid < currentMass)
                    {
                        stack.Pop();
                        continue;
                    }
                    else if (topAsteroid == currentMass)
                    {
                        stack.Pop();
                        alive = false;
                        break;
                    }
                    else
                    {
                        alive = false;
                        break;
                    }
                }
                
                if (alive) 
                {
                    stack.Push(v);
                }
            }
            
            return stack.Reverse().ToArray();
        }
    }
}
