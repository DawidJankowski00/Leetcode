using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
{
    public int SnakesAndLadders(int[][] board)
    {
        int n = board.Length;
        int end = n * n;
        
        Dictionary<int, int> tp = new Dictionary<int, int>();

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                int rowFromBottom = n - 1 - i;
                int currentSquare;

                if (rowFromBottom % 2 == 0)
                {
                    currentSquare = rowFromBottom * n + (j + 1);
                }
                else
                {
                    currentSquare = rowFromBottom * n + (n - j);
                }

                int boardValue = board[i][j];
                
                if (boardValue != -1)
                {
                    tp[currentSquare] = boardValue;
                }
                else
                {
                    tp[currentSquare] = currentSquare;
                }
            }
        }

        Queue<(int square, int moves)> queue = new Queue<(int square, int moves)>();
        queue.Enqueue((1, 0)); 
        
        HashSet<int> visited = new HashSet<int> { 1 };

        while (queue.Count > 0)
        {
            var (q, s) = queue.Dequeue(); 
            
            if (q == end)
            {
                return s;
            }
            
            for (int i = 1; i <= 6; i++)
            {
                int nextSquareCandidate = q + i;
                
                if (nextSquareCandidate <= end)
                {
                    int targetSquare = tp[nextSquareCandidate];
                    
                    if (!visited.Contains(targetSquare))
                    {
                        visited.Add(targetSquare);
                        queue.Enqueue((targetSquare, s + 1));
                    }
                }
            }
        }
        
        return -1; 
    }
}
}
