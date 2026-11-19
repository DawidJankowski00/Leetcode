using System;

public class Solution {
    public int MinimizeSum(int[] nums) {
        if (nums.Length == 3) {
            return 0;
        }

        int min1 = int.MaxValue, min2 = int.MaxValue, min3 = int.MaxValue;
        int max1 = int.MinValue, max2 = int.MinValue, max3 = int.MinValue;

        foreach (int num in nums) {
            if (num <= min1) {
                min3 = min2;
                min2 = min1;
                min1 = num;
            } else if (num <= min2) {
                min3 = min2;
                min2 = num;
            } else if (num < min3) {
                min3 = num;
            }

            if (num >= max1) {
                max3 = max2;
                max2 = max1;
                max1 = num;
            } else if (num >= max2) {
                max3 = max2;
                max2 = num;
            } else if (num > max3) {
                max3 = num;
            }
        }

        int a = max1 - min3;
        int b = max2 - min2;
        int c = max3 - min1;

        return Math.Min(a, Math.Min(b, c));
    }
}
