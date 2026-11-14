public class Solution {
    public int MinimumSumSubarray(IList<int> nums, int l, int r) {
        int result = int.MaxValue;
        int n = nums.Count;

        for (int i = l; i <= r; i++) {
            int curr = 0;
            for (int k = 0; k < i; k++) {
                curr += nums[k];
            }

            if (curr > 0) {
                result = Math.Min(result, curr);
            }

            for (int j = i; j < n; j++) {
                curr += nums[j];
                curr -= nums[j - i];
                if (curr > 0) {
                    result = Math.Min(result, curr);
                }
            }
        }

        return result != int.MaxValue ? result : -1;
    }
}