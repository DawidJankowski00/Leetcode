using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public void GameOfLife(int[][] board)
        {
            int n = board.Length;
            int m = board[0].Length;
            int[][] directions = new int[][]
            {
                new[] {0, 1}, new[] {1, 1}, new[] {1, 0}, new[] {1, -1},
                new[] {0, -1}, new[] {-1, -1}, new[] {-1, 0}, new[] {-1, 1}
            };
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    int tmp = 0;
                    foreach (var dir in directions)
                    {
                        int x = i + dir[0], y = j + dir[1];
                        if (x >= 0 && x < n && y >= 0 && y < m)
                        {
                            if (board[x][y] == 1 || board[x][y] == 3)
                                tmp++;
                        }
                    }
                    if (board[i][j] == 0 && tmp == 3) board[i][j] = 2;
                    if (board[i][j] == 1 && tmp != 2 && tmp != 3) board[i][j] = 3;
                    
                }
            }
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    if (board[i][j] == 2) board[i][j] = 1;
                    if (board[i][j] == 3) board[i][j] = 0;
                }
            }
        }
    }
}
