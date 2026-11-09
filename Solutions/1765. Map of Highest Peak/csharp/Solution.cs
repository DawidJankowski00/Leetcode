using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public int[][] HighestPeak(int[][] isWater)
        {
            int n = isWater.Length;
            int m = isWater[0].Length;
            int[][] result = new int[n][];
            Queue<(int x, int y)> queue = new Queue<(int x, int y)>();

            for (int i = 0; i < n; i++)
            {
                result[i] = new int[m];
                Array.Fill(result[i], -1);
            }

            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    if (isWater[i][j] == 1)
                    {
                        result[i][j] = 0;
                        queue.Enqueue((i, j));
                    }
                }
            }
            int[][] directions = new int[][]
            {
                new int[] {-1, 0}, new int[] {1, 0}, new int[] {0, -1}, new int[] {0, 1}
            };
            while (queue.Count > 0)
            {
                var q = queue.Dequeue();
                int x = q.x;
                int y = q.y;
                foreach (var d in directions)
                {
                    var nx = x + d[0];
                    var ny = y + d[1];
                    if (0 <= nx && 0 <= ny && nx < n && ny < m && result[nx][ny] == -1)
                    {
                        result[nx][ny] = result[x][y] + 1;
                        queue.Enqueue((nx, ny));
                    }
                }
            }
            return result;
        }
    }
}
