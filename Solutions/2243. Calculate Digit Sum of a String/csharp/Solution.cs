public class Solution {
    public string DigitSum(string s, int k) {
        while (s.Length > k) {
            StringBuilder sb = new StringBuilder();
            
            for (int i = 0; i < s.Length; i += k) {
                int sum = 0;
                for (int j = i; j < i + k && j < s.Length; j++) {
                    sum += s[j] - '0';
                }
                sb.Append(sum);
            }
            
            s = sb.ToString();
        }
        
        return s;
    }
}