using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sample
{
    public class Solution 
    {
        public long MinOperations(int[] nums, int x, int k) 
        {
            long[] windowPenalties = ComputeWindowCosts(nums, x);
            int totalLen = nums.Length;
            
            long[] dpState = new long[totalLen + 1];
            long[] nextDp = new long[totalLen + 1];
            long inf = long.MaxValue / 3;

            for (int step = 0; step < k; step++) 
            {
                long runningMin = inf;
                for (int i = 0; i <= totalLen; i++) 
                {
                    if (i >= x) 
                    {
                        long candidate = dpState[i - x] + windowPenalties[i - x];
                        if (candidate < runningMin) 
                        {
                            runningMin = candidate;
                        }
                    }
                    nextDp[i] = runningMin;
                }
                
                var temp = dpState;
                dpState = nextDp;
                nextDp = temp;
            }

            return dpState[totalLen];
        }

        private long[] ComputeWindowCosts(int[] elements, int span) 
        {
            int halfLen = span / 2;
            int isOdd = span & 1;
            int n = elements.Length;

            var lowerHeap = new PriorityQueue<int, long>();
            var upperHeap = new PriorityQueue<int, long>();

            byte[] location = new byte[n];

            long lowerSum = 0;
            long totalSum = 0;
            int lowerValidCount = 0;

            void PruneLower() 
            {
                while (lowerHeap.Count > 0 && location[lowerHeap.Peek()] != 1) 
                {
                    lowerHeap.Dequeue();
                }
            }

            void PruneUpper() 
            {
                while (upperHeap.Count > 0 && location[upperHeap.Peek()] != 2) 
                {
                    upperHeap.Dequeue();
                }
            }

            void Rebalance() 
            {
                while (lowerValidCount > halfLen) 
                {
                    PruneLower();
                    int idx = lowerHeap.Dequeue();
                    location[idx] = 2;
                    lowerValidCount--;
                    lowerSum -= elements[idx];
                    upperHeap.Enqueue(idx, elements[idx]);
                }
                
                while (lowerValidCount < halfLen) 
                {
                    PruneUpper();
                    int idx = upperHeap.Dequeue();
                    location[idx] = 1;
                    lowerValidCount++;
                    lowerSum += elements[idx];
                    lowerHeap.Enqueue(idx, -(long)elements[idx]);
                }
            }

            long[] allCosts = new long[n - span + 1];

            for (int i = 0; i < span; i++) 
            {
                totalSum += elements[i];
                location[i] = 2;
                upperHeap.Enqueue(i, elements[i]);
            }
            Rebalance();

            long GetCurrentCost() 
            {
                long medianVal = 0;
                if (isOdd == 1) 
                {
                    PruneUpper();
                    medianVal = elements[upperHeap.Peek()];
                }
                return totalSum - 2 * lowerSum - medianVal;
            }

            allCosts[0] = GetCurrentCost();

            for (int i = span; i < n; i++) 
            {
                int outIdx = i - span;
                int inVal = elements[i];
                int outVal = elements[outIdx];

                totalSum += inVal - outVal;

                if (location[outIdx] == 1) 
                {
                    lowerValidCount--;
                    lowerSum -= outVal;
                }
                location[outIdx] = 0;

                PruneUpper();
                if (upperHeap.Count > 0 && inVal >= elements[upperHeap.Peek()]) 
                {
                    location[i] = 2;
                    upperHeap.Enqueue(i, inVal);
                } 
                else 
                {
                    location[i] = 1;
                    lowerValidCount++;
                    lowerSum += inVal;
                    lowerHeap.Enqueue(i, -(long)inVal);
                }

                Rebalance();
                allCosts[i - span + 1] = GetCurrentCost();
            }

            return allCosts;
        }
    }
}
