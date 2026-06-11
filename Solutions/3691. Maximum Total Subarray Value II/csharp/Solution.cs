using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class SubarrayValueTable 
    {
        private readonly int[][] minTable;
        private readonly int[][] maxTable;

        public SubarrayValueTable(int[] arr) 
        {
            int size = arr.Length;
            int levels = Log2(size) + 1;

            minTable = new int[levels][];
            maxTable = new int[levels][];
            for (int i = 0; i < levels; i++) 
            {
                minTable[i] = new int[size];
                maxTable[i] = new int[size];
            }

            for (int i = 0; i < size; i++) 
            {
                minTable[0][i] = maxTable[0][i] = arr[i];
            }

            for (int i = 1; i < levels; i++) 
            {
                int span = 1 << i;
                int halfSpan = 1 << (i - 1);
                for (int j = 0; j <= size - span; j++) 
                {
                    minTable[i][j] = Math.Min(minTable[i - 1][j], minTable[i - 1][j + halfSpan]);
                    maxTable[i][j] = Math.Max(maxTable[i - 1][j], maxTable[i - 1][j + halfSpan]);
                }
            }
        }

        public int GetValue(int start, int end) 
        {
            int k = Log2(end - start + 1);
            int span = 1 << k;

            int rangeMax = Math.Max(maxTable[k][start], maxTable[k][end - span + 1]);
            int rangeMin = Math.Min(minTable[k][start], minTable[k][end - span + 1]);

            return rangeMax - rangeMin;
        }

        private int Log2(int value) 
        {
            return 31 - System.Numerics.BitOperations.LeadingZeroCount((uint)value);
        }
    }

    public class Solution 
    {
        public long MaxTotalValue(int[] nums, int k) 
        {
            int n = nums.Length;
            SubarrayValueTable valueFinder = new SubarrayValueTable(nums);

            var maxHeap = new PriorityQueue<(int left, int right), int>(Comparer<int>.Create((a, b) => b.CompareTo(a)));

            for (int i = 0; i < n; i++) 
            {
                int val = valueFinder.GetValue(i, n - 1);
                maxHeap.Enqueue((i, n - 1), val);
            }

            long totalMaxValue = 0;

            for (int i = 0; i < k; i++) 
            {
                if (maxHeap.Count == 0) 
                    break;

                if (!maxHeap.TryDequeue(out var current, out int currentValue)) 
                    break;

                if (currentValue == 0) 
                    break;

                totalMaxValue += currentValue;

                if (current.left < current.right) 
                {
                    int nextVal = valueFinder.GetValue(current.left, current.right - 1);
                    maxHeap.Enqueue((current.left, current.right - 1), nextVal);
                }
            }

            return totalMaxValue;
        }
    }
}
