using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
    {
        public bool IsValidSudoku(char[][] board)
        {
            Dictionary<char, int>[] rows = new Dictionary<char, int>[9];
            Dictionary<char, int>[] cols = new Dictionary<char, int>[9];
            Dictionary<char, int>[] box = new Dictionary<char, int>[9];
            for (int i = 0; i < 9; i++)
            {
                rows[i] = new Dictionary<char, int>();
                cols[i] = new Dictionary<char, int>();
                box[i] = new Dictionary<char, int>();
            }
            for (int i = 0; i < board.Length; i++)
            {
                for (int j = 0; j < board[i].Length; j++)
                {
                    if (board[i][j] != '.')
                    {
                        if (rows[i].ContainsKey(board[i][j])) return false;
                        rows[i][board[i][j]] = 1;
                        if (cols[j].ContainsKey(board[i][j])) return false;
                        cols[j][board[i][j]] = 1;
                        int k = (i / 3) * 3 + j/3;
                        if (box[k].ContainsKey(board[i][j])) return false;
                        box[k][board[i][j]] = 1;

                    }
                }
            }
            return true;

        }
    }
}
