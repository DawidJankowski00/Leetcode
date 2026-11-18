public class Solution {
    public int MinChanges(string s) {
        int result = 0;
        for (int i = 0; i < s.Length; i += 2)
        {
            if (s[i] != s[i+1]) result++;
        }
        return result;
    }
}
