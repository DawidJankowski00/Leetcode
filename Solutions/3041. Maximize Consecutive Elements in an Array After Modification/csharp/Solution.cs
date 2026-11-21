using System;
using System.Collections.Generic;

public class Solution {
    public int MaxSelectedElements(int[] nums) {
        Array.Sort(nums);
        var dp = new Dictionary<int, int>();
        int maxLen = 0;

        foreach (int x in nums) {
            // Aktualizujemy x + 1 PRZED x, aby nie użyć tego samego elementu dwa razy
            int lenPlusOne = dp.GetValueOrDefault(x, 0) + 1;
            int lenCurrent = dp.GetValueOrDefault(x - 1, 0) + 1;

            dp[x + 1] = lenPlusOne;
            dp[x] = lenCurrent;

            if (lenPlusOne > maxLen) maxLen = lenPlusOne;
            if (lenCurrent > maxLen) maxLen = lenCurrent;
        }

        return maxLen;
    }
}