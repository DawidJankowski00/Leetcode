using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public string PredictPartyVictory(string senate) {
            Queue<int> qr = new Queue<int>();
            Queue<int> qd = new Queue<int>();
            int n = senate.Length;
            for (int i = 0; i < n; i++)
            {
                if (senate[i] == 'R') qr.Enqueue(i);
                else qd.Enqueue(i);
            }
            while (qr.Count > 0 && qd.Count > 0)
            {
                int player_R = qr.Dequeue();
                int player_D = qd.Dequeue();
                if (player_R < player_D) qr.Enqueue(n);
                else qd.Enqueue(n);
                n++;
            }
            if (qr.Count > 0) return "Radiant";
            return "Dire";
        }
    }
}
