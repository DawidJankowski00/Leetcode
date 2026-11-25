using System;

public class Solution {
    public int SmallestUniqueSubarray(int[] nums) {
        int n = nums.Length;
        if (n <= 1) return n;

        int m = n + 1;
        int[] s = new int[m];
        int maxVal = 0;
        for (int i = 0; i < n; i++) {
            s[i] = nums[i];
            if (nums[i] > maxVal) maxVal = nums[i];
        }
        s[n] = 0;

        int alphabet = Math.Max(m, maxVal + 1);
        int[] p = new int[m];
        int[] c = new int[m];
        int[] cnt = new int[alphabet];

        for (int i = 0; i < m; i++) cnt[s[i]]++;
        for (int i = 1; i <= maxVal; i++) cnt[i] += cnt[i - 1];
        for (int i = m - 1; i >= 0; i--) p[--cnt[s[i]]] = i;

        c[p[0]] = 0;
        int classes = 1;
        for (int i = 1; i < m; i++) {
            if (s[p[i]] != s[p[i - 1]]) classes++;
            c[p[i]] = classes - 1;
        }

        int[] pn = new int[m];
        int[] cn = new int[m];
        for (int h = 0; (1 << h) < m; h++) {
            int len = 1 << h;
            for (int i = 0; i < m; i++) {
                int idx = p[i] - len;
                pn[i] = idx < 0 ? idx + m : idx;
            }

            Array.Clear(cnt, 0, classes);
            for (int i = 0; i < m; i++) cnt[c[pn[i]]]++;
            for (int i = 1; i < classes; i++) cnt[i] += cnt[i - 1];
            for (int i = m - 1; i >= 0; i--) p[--cnt[c[pn[i]]]] = pn[i];

            cn[p[0]] = 0;
            classes = 1;
            for (int i = 1; i < m; i++) {
                int cur2 = p[i] + len;
                if (cur2 >= m) cur2 -= m;
                int prev2 = p[i - 1] + len;
                if (prev2 >= m) prev2 -= m;

                if (c[p[i]] != c[p[i - 1]] || c[cur2] != c[prev2]) {
                    classes++;
                }
                cn[p[i]] = classes - 1;
            }

            (c, cn) = (cn, c);
            if (classes == m) break;
        }

        int[] rank = new int[n];
        for (int i = 1; i < m; i++) {
            rank[p[i]] = i - 1;
        }

        int[] lcp = new int[n - 1];
        int k = 0;
        for (int i = 0; i < n; i++) {
            int r = rank[i];
            if (r == n - 1) {
                k = 0;
                continue;
            }
            int j = p[r + 2];
            while (i + k < n && j + k < n && nums[i + k] == nums[j + k]) {
                k++;
            }
            lcp[r] = k;
            if (k > 0) k--;
        }

        int ans = n;
        for (int r = 0; r < n; r++) {
            int leftLcp = r > 0 ? lcp[r - 1] : 0;
            int rightLcp = r < n - 1 ? lcp[r] : 0;
            int needed = Math.Max(leftLcp, rightLcp) + 1;
            int suffixLen = n - p[r + 1];

            if (needed <= suffixLen && needed < ans) {
                ans = needed;
            }
        }

        return ans;
    }
}