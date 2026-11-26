class Solution {
    public boolean canAliceWin(int n) {
        boolean result = false;
        for (int i = 10; i > 1; i -= 2) {
            n -= i;
            if (n >= 0) {
                result = true;
            } else {
                result = false;
                break;
            }
            
            n -= (i - 1);
            if (n >= 0) {
                result = false;
            } else {
                break;
            }
        }
        return result;
    }
}