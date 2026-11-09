using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int MinimumObstacles(int[][] grid)
        {
            int m = grid.Length;
            int n = grid[0].Length;
            int[][] directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
            LinkedList<(int x, int y, int dist)> queue = new LinkedList<(int x, int y, int dist)>();
            queue.AddLast((0,0,0));
            bool[,] visited = new bool[m, n];
            visited[0, 0] = true;

            while (queue.Count > 0)
            {
                var tmp = queue.First.Value;
                queue.RemoveFirst();
                int x = tmp.x;
                int y = tmp.y;
                int dist = tmp.dist;
                if (x == m-1 && y == n - 1)
                {
                    return dist;
                }
                foreach (var v in directions) 
                {
                    int newx = x + v[0];
                    int newy = y + v[1];
                    if (newx >= 0 && newx < m && newy >= 0 && newy < n)
                    {
                        if (!visited[newx, newy])
                        {
                            visited[newx, newy] = true;
                            if (grid[newx][newy] == 0)
                            {
                                queue.AddFirst((newx, newy, dist));
                            }
                            else
                            {
                                queue.AddLast((newx, newy, dist+1));
                            }
                        }
                    }
                }
            }
            return -1;
        }
    }
}
