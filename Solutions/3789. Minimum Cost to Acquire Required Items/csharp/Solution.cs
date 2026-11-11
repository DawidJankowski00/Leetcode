public class Solution {
    public long MinimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long c1 = cost1;
        long c2 = cost2;
        long cb = costBoth;
        long n1 = need1;
        long n2 = need2;

        c1 = Math.Min(c1, cb);
        c2 = Math.Min(c2, cb);

        long common = Math.Min(n1, n2);
        long costForCommon = common * Math.Min(c1 + c2, cb);
        long costRemaining = (n1 - common) * c1 + (n2 - common) * c2;

        return costForCommon + costRemaining;
    }
}
