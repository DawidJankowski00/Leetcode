using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    using System;
using System.Collections.Generic;

public class Solution
{
    public int TrapRainWater(int[][] heightMap)
    {
        int rows = heightMap.Length;
        int cols = heightMap[0].Length;
        if (rows < 3 || cols < 3)
            return 0;

        int waterTrapped = 0;
        var minHeap = new PriorityQueue<(int height, int x, int y), int>();

        for (int r = 0; r < rows; r++)
        {
            for (int c = 0; c < cols; c++)
            {
                if (r == 0 || r == rows - 1 || c == 0 || c == cols - 1)
                {
                    minHeap.Enqueue((heightMap[r][c], r, c), heightMap[r][c]);
                    heightMap[r][c] = -1;
                }
            }
        }

        int maxLevel = 0;
        int[][] directions = new int[][] {
            new int[] {-1, 0}, new int[] {1, 0}, new int[] {0, -1}, new int[] {0, 1}
        };

        while (minHeap.Count > 0)
        {
            var (height, x, y) = minHeap.Dequeue();
            maxLevel = Math.Max(maxLevel, height);

            foreach (var dir in directions)
            {
                int nx = x + dir[0];
                int ny = y + dir[1];

                if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && heightMap[nx][ny] != -1)
                {
                    if (heightMap[nx][ny] < maxLevel)
                    {
                        waterTrapped += maxLevel - heightMap[nx][ny];
                    }

                    minHeap.Enqueue((heightMap[nx][ny], nx, ny), heightMap[nx][ny]);
                    heightMap[nx][ny] = -1;
                }
            }
        }

        return waterTrapped;
    }
}

}
