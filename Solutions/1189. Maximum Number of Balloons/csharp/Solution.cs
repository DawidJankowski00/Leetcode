using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution {
        public int MaxNumberOfBalloons(string text) {
            // Tworzymy słownik częstotliwości (odpowiednik Counter)
            var freq = text.GroupBy(c => c)
                        .ToDictionary(g => g.Key, g => g.Count());

            // Pomocnicza funkcja, aby uniknąć błędów, gdy litery nie ma w tekście
            int GetCount(char c) => freq.ContainsKey(c) ? freq[c] : 0;

            // Zwracamy minimum pasujące do słowa "balloon"
            return Math.Min(
                GetCount('b'),
                Math.Min(GetCount('a'),
                Math.Min(GetCount('n'),
                Math.Min(GetCount('l') / 2, GetCount('o') / 2)))
            );
        }
    }
}
