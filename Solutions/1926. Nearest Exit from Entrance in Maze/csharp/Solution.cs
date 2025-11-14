using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution 
    {
        public int NearestExit(char[][] maze, int[] entrance) 
        {
            int mazeN = maze.Length;
            int mazeM = maze[0].Length;
            
            (int, int)[] directions = { (0, 1), (1, 0), (0, -1), (-1, 0) };
            
            var queue = new Queue<(int, int)>();
            var visited = new HashSet<(int, int)>();
            
            int startX = entrance[0];
            int startY = entrance[1];
            
            queue.Enqueue((startX, startY));
            visited.Add((startX, startY));
            
            int result = 0;

            while (queue.Count > 0)
            {
                int n = queue.Count;
                result++;

                for (int i = 0; i < n; i++)
                {
                    (int x, int y) = queue.Dequeue();
                    
                    foreach (var (xd, yd) in directions)
                    {
                        int nx = xd + x;
                        int ny = yd + y;

                        bool isInBounds = nx >= 0 && ny >= 0 && nx < mazeN && ny < mazeM;
                        
                        if (isInBounds && maze[nx][ny] != '+')
                        {
                            bool isOnBorder = (nx == 0 || ny == 0 || nx == mazeN - 1 || ny == mazeM - 1);
                            bool isNotEntrance = (nx != startX || ny != startY);
                            
                            if (isOnBorder && isNotEntrance)
                            {
                                return result;
                            }
                                
                            if (!visited.Contains((nx, ny)))
                            {
                                visited.Add((nx, ny));
                                queue.Enqueue((nx, ny));
                            }
                        }
                    }
                }
            }
                
            return -1;
        }
    }
}
