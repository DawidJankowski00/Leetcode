using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public void Solve(char[][] board)
        {
            int m = board.Length;
            int n = board[0].Length;
            void dfs(int x, int y)
            {
                if (x < 0 || y < 0 || x >= m || y >= n || board[x][y] != 'O')
                    return;

                board[x][y] = '0';
                dfs(x + 1, y);
                dfs(x - 1, y);
                dfs(x, y + 1);
                dfs(x, y - 1);
            }

            for (int i = 0; i < m; i++)
            {
                dfs(i, 0);
                dfs(i, n-1);
            }
            for(int i = 0;i < n; i++)
            {
                dfs(0, i);
                dfs(m-1, i);
            }
            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (board[i][j] == 'O') board[i][j] = 'X';
                    if (board[i][j] == '0') board[i][j] = 'O';
                }
            }   
        }
    }
}
