using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int OrangesRotting(int[][] grid) {
            int rows = grid.Length;
            int cols = grid[0].Length;
            Queue<(int, int)> queue = new Queue<(int, int)>();
            int freshCount = 0;

            for (int r = 0; r < rows; r++) {
                for (int c = 0; c < cols; c++) {
                    if (grid[r][c] == 2) {
                        queue.Enqueue((r, c));
                    } else if (grid[r][c] == 1) {
                        freshCount++;
                    }
                }
            }

            if (freshCount == 0) return 0;

            int minutes = 0;
            int[][] directions = new int[][] {
                new int[] { -1, 0 },
                new int[] { 1, 0 },
                new int[] { 0, -1 },
                new int[] { 0, 1 }
            };

            while (queue.Count > 0 && freshCount > 0) {
                int size = queue.Count;
                for (int i = 0; i < size; i++) {
                    var (r, c) = queue.Dequeue();
                    foreach (var dir in directions) {
                        int nr = r + dir[0];
                        int nc = c + dir[1];
                        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                            grid[nr][nc] = 2;
                            freshCount--;
                            queue.Enqueue((nr, nc));
                        }
                    }
                }
                minutes++;
            }

            return freshCount == 0 ? minutes : -1;
        }
    }
}