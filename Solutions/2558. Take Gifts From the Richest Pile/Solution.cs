using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution
{
    public int PickGifts(int[] gifts, int k)
    {
        PriorityQueue<int, int> maxHeap = new PriorityQueue<int, int>(Comparer<int>.Create((a, b) => b.CompareTo(a)));
        foreach (int gift in gifts)
        {
            maxHeap.Enqueue(gift, gift);
        }

        int i = 0;
        while (i < k && maxHeap.TryDequeue(out int maxGift, out _))
        {
            int newGift = (int)Math.Sqrt(maxGift);
            maxHeap.Enqueue(newGift, newGift);
            i++;
        }
        int total = 0;
        while (maxHeap.TryDequeue(out int gift, out _))
        {
            total += gift;
        }

        return total;
    }
}
}
