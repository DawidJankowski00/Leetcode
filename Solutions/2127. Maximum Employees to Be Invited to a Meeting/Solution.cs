using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
{
    public int MaximumInvitations(int[] favorite)
    {
        int n = favorite.Length;
        int[] inDegree = new int[n];
        int[] lengths = new int[n];
        bool[] processed = new bool[n];

        // Obliczanie stopnia wejściowego dla każdego węzła
        foreach (var person in favorite)
        {
            inDegree[person]++;
        }

        // Kolejka dla węzłów o stopniu wejściowym 0
        Queue<int> queue = new Queue<int>();
        for (int i = 0; i < n; i++)
        {
            if (inDegree[i] == 0)
            {
                queue.Enqueue(i);
            }
        }

        // Przetwarzanie węzłów z kolejki
        while (queue.Count > 0)
        {
            int current = queue.Dequeue();
            processed[current] = true;
            int nextPerson = favorite[current];
            lengths[nextPerson] = Math.Max(lengths[nextPerson], lengths[current] + 1);
            inDegree[nextPerson]--;
            if (inDegree[nextPerson] == 0)
            {
                queue.Enqueue(nextPerson);
            }
        }

        int largestCycle = 0;
        int combinedPairs = 0;

        // Wyszukiwanie cykli
        for (int index = 0; index < n; index++)
        {
            if (!processed[index])
            {
                int cycleSize = 0;
                int node = index;

                while (!processed[node])
                {
                    processed[node] = true;
                    node = favorite[node];
                    cycleSize++;
                }

                if (cycleSize == 2)
                {
                    combinedPairs += 2 + lengths[index] + lengths[favorite[index]];
                }
                else
                {
                    largestCycle = Math.Max(largestCycle, cycleSize);
                }
            }
        }

        return Math.Max(largestCycle, combinedPairs);
    }
}
}
