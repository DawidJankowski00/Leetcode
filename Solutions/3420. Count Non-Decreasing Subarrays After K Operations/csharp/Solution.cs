using System.Collections.Generic;

public class Solution {
    public long CountNonDecreasingSubarrays(int[] nums, int k) {
        int n = nums.Length;
        long result = 0;
        long ops = 0;
        var dq = new LinkedList<int[]>();
        
        int r = n - 1;
        for (int l = n - 1; l >= 0; l--) {
            int currVal = nums[l];
            int count = 1;
            
            while (dq.Count > 0 && dq.First.Value[0] <= currVal) {
                int[] prev = dq.First.Value;
                dq.RemoveFirst();
                ops += (long)(currVal - prev[0]) * prev[1];
                count += prev[1];
            }
            
            dq.AddFirst(new int[] { currVal, count });
            
            while (ops > k) {
                int[] last = dq.Last.Value;
                int rightmostCeil = last[0];
                ops -= (rightmostCeil - nums[r]);
                
                last[1]--;
                if (last[1] == 0) {
                    dq.RemoveLast();
                }
                r--;
            }
            
            result += (r - l + 1);
        }
        
        return result;
    }
}